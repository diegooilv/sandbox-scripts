import { Client } from "@gradio/client"; // ^1.11.0

async function main(message) {
    if(!message){
        return "Não deixe o prompt em branco!"
    }
    try {
        const client = await Client.connect("Qwen/Qwen2.5-Max-Demo");

        const result = await client.predict("/model_chat", { 		
            query: message, 		
            history: [],  
            system: "Responda da melhor maneira possível!!",  // Aq fica as regras ou pedidos do sistema...
        });

        console.log(result.data[1][0][1]);
        return result.data[1][0][1];

    } catch (error) {
        console.error("Erro ao conectar ou enviar requisição:", error);
    }
}

main("Me explique sobre o discord.");