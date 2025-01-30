const { inspect } = require("util");
const vm = require("vm");
const Command = require("../../Handlers/command.js");

// Bloqueio de módulos sensíveis
const BLACKLIST = new Set([
  "child_process", "cluster", "crypto", "dns", "domain", "fs", "http2",
  "https", "net", "os", "path", "perf_hooks", "process", "querystring",
  "readline", "repl", "tls", "tty", "v8", "vm", "worker_threads", "zlib"
]);

module.exports = class extends Command {
  constructor(client) {
    super(client, {
      name: "eval",
      aliases: ["e", "ev"],
      description: "Dev - Executar comandos através do Discord.",
      devOnly: true,
      guarded: true
    });
  }

  async execute(message, args) {
    const code = this.cleanCode(args.join(" "));
    
    if (!code) {
      return message.channel.send("❌ Forneça um código para execução.");
    }

    try {
      // Configuração do ambiente seguro
      const sandbox = this.createSandbox(message);
      const context = vm.createContext(sandbox);
      
      // Execução controlada
      const result = await this.runInContext(code, context);
      await this.sendResult(message, result);
      
    } catch (error) {
      await this.handleError(message, error);
    } finally {
      this.cleanupResources();
    }
  }

  cleanCode(code) {
    return code
      .replace(/^```(js|javascript)?|```$/g, "")
      .trim();
  }

  createSandbox(message) {
    return {
      // Objetos permitidos
      console: this.safeConsole(),
      message: message,
      client: this.sanitizeClient(),
      args: message.args,
      
      // Funções seguras
      setTimeout: null,
      setInterval: null,
      clearTimeout: null,
      clearInterval: null,
      
      // Primitivos seguros
      Math: Object.create(null),
      Date: this.safeDate(),
      JSON: Object.create(JSON),
      Buffer: null,
      
      // Bloqueio de acesso indireto
      global: null,
      process: null,
      require: this.safeRequire(),
      module: null,
      import: null
    };
  }

  safeRequire() {
    return (name) => {
      if (BLACKLIST.has(name)) {
        throw new Error(`Acesso negado ao módulo: ${name}`);
      }
      return require(name);
    };
  }

  safeConsole() {
    const consoleProxy = {};
    const methods = ["log", "warn", "error", "info", "debug"];
    
    for (const method of methods) {
      consoleProxy[method] = (...args) => {
        const output = args.map(arg => inspect(arg, { depth: 0 }));
        console[method](`[Sandbox]`, ...output);
      };
    }
    return consoleProxy;
  }

  async runInContext(code, context) {
    const script = new vm.Script(
      `(async () => { ${code} })()`,
      {
        timeout: 3000,
        lineOffset: -2,
        displayErrors: false
      }
    );

    return script.runInContext(context);
  }

  async sendResult(message, result) {
    const inspected = inspect(result, {
      depth: 2,
      maxArrayLength: 10,
      showProxy: false,
      compact: true,
      breakLength: 50
    });

    const chunks = this.splitMessage(inspected);
    for (const chunk of chunks) {
      await message.channel.send(`\`\`\`js\n${chunk}\`\`\``);
    }
  }

  splitMessage(content, maxLength = 1900) {
    const chunks = [];
    while (content.length > 0) {
      chunks.push(content.slice(0, maxLength));
      content = content.slice(maxLength);
    }
    return chunks;
  }

  handleError(message, error) {
    const errorInfo = {
      name: error.name,
      message: error.message,
      stack: error.stack.split("\n")[0]
    };

    console.error("[EVAL ERROR]", error);
    return message.channel.send(`\`\`\`js\n${inspect(errorInfo)}\`\`\``);
  }

  cleanupResources() {
    // Limpeza de recursos e garbage collection
    if (global.gc) {
      global.gc();
    }
  }

  sanitizeClient() {
    const client = this.client;
    return new Proxy(client, {
      get(target, prop) {
        const forbidden = ["token", "destroy", "login", "options"];
        if (forbidden.includes(prop)) {
          throw new Error(`Acesso negado à propriedade: ${prop}`);
        }
        return target[prop];
      }
    });
  }

  safeDate() {
    const date = new Date();
    return new Proxy(Date, {
      construct(target, args) {
        return new target(...args);
      },
      get() {
        return date.getTime();
      }
    });
  }
};