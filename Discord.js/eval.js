/*const { inspect } = require("util");
const vm = require("vm");
const Command = require("../../Handlers/command.js");
*/
module.exports = class extends Command {
  /*constructor(client) {
    super(client, {
      name: "eval",
      aliases: ["e", "ev"],
      description: "Dev - Executar comandos através do Discord.",
      devOnly: true,
    });

    this.client = client;
  }*/
  async execute(message, args) {
    const code = args.join(" ");

    if (!code) {
      return message.channel.send("Por favor, forneça um código para executar.");
    }

    try {
      Object.defineProperty(this.client, "token", {
        value: undefined,
        writable: false,
        configurable: false,
        enumerable: false,
      });

      const sandbox = {
        console,
        message,
        args,
        client: this.client,
        setTimeout,
        setInterval,
        clearTimeout,
        clearInterval,
        Math,
        Date,
        Buffer: undefined,
        process: undefined,
        require: undefined,
        global: undefined,
        Array,
        Object,
        String,
        Number,
        Boolean,
        RegExp,
        Function,
        JSON,
        fs: undefined,
        child_process: undefined,
        os: undefined,
        vm: undefined,
      };

      const context = vm.createContext(sandbox);

      const asyncCode = `
        (async () => {
          try {
            return ${code};
          } catch (err) {
            throw err;
          }
        })()
      `;

      const script = new vm.Script(asyncCode, { timeout: 1000 });

      const result = await script.runInContext(context);

      const formattedResult = inspect(result, { depth: 1 }).substring(0, 1990);
      message.channel.send(`\`\`\`js\n${formattedResult}\`\`\``);
    } catch (error) {
      const errorMessage = error.toString().substring(0, 1990);
      message.channel.send(`\`\`\`js\n${errorMessage}\`\`\``);
    }
  }
};
