const fetch = require('node-fetch'); 
// TODO: Make sure to insert your OpenAI key here:
const openAiApiKey = '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';

async function run() {

    // Call OpenAI's API
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${openAiApiKey}`,
        },
        body: JSON.stringify({
            // The model currently used by ChatGPT
            'model': 'gpt-3.5-turbo',
            // The conversation history of this chat. Let's start by saying hi.
            'messages': [{
                'role': 'user',
                'content': '5 Fascinating Facts about Polar Bears. Make a numbered list of 5 short sentences.'
            }],
        }),
    });

    // Catch any unsuccessful HTTP responses
    if (!response.ok) {
        console.error(`Error: OpenAI returned status code ${response.status}. `
            + `Make sure that you've provided a valid OpenAI API key`);
        process.exit(1);
    }

    // Parse ChatGPT's JSON response as a JavaScript object
    const data = await response.json();

    // Print the results to the console
    console.log(JSON.stringify(data));
    console.log(data.choices.messages.content);
}

run()
    .catch(error => console.error(error));