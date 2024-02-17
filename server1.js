const Creatomate = require('creatomate');
const client = new Creatomate.Client('a59cc61d043143eba541f18c74763517781e3a9d295e6c64a3b6e7db75f503ff37f65730881ab6f9ffb9eac1dda76f1b');

const options = {
    // The ID of the template that you created in the template editor
    templateId: 'a224e67e-a34d-4c1d-8e3f-545d3de63553',

    // Modifications that you want to apply to the template
    modifications: {
        "Review-Text": "This content is changed by api , and this is best ai generator i have ever seen"
    },
};

console.log('Please wait while your video is being rendered...');

client.render(options)
    .then((renders) => {
        console.log('Completed:', renders);
    })
    .catch((error) => console.error(error));



// curl - s - X POST https://api.creatomate.com/v1/renders \
// -H 'Authorization: Bearer a59cc61d043143eba541f18c74763517781e3a9d295e6c64a3b6e7db75f503ff37f65730881ab6f9ffb9eac1dda76f1b' \
// -H 'Content-Type: application/json' \
// --data - binary @- << EOF
    // {
    // "template_id": "a224e67e-a34d-4c1d-8e3f-545d3de63553",
    // "modifications": {
        // "3a994049-9d90-435a-bb43-51d7264c0eeb": "https://creatomate.com/files/assets/1b704a73-8d4b-49f8-ba5d-b28c1eb9c795",
        // "17279a2c-1059-4afb-826d-58a5c01c8499": "https://creatomate.com/files/assets/1b704a73-8d4b-49f8-ba5d-b28c1eb9c795",
        // "Profile-Picture": "https://creatomate.com/files/assets/d6628425-8e35-4fee-9de8-a18d21309546",
        // "Name": "Elisabeth Parker",
        // "Date.text.Date": "",
        // "Review-Text": "If you're looking for a secluded and peaceful retreat, this cabin in the woods is the perfect choice! 🌲❤️"
    // }
// }
// EOF