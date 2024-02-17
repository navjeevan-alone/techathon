const axios = require('axios'); // Install Axios using: `npm install axios`
const data = JSON.stringify({
    "id": "bfaf0138-0bf1-4495-acfe-f31ac3e43f52",
    "merge": [
        {
            "find": "ADDRESS",
            "replace": "192 STOREY STREET"
        },
        {
            "find": "SUBURB",
            "replace": "MAROUBRA"
        },
        {
            "find": "STATE",
            "replace": "NSW"
        },
        {
            "find": "POSTCODE",
            "replace": "2035"
        },
        {
            "find": "BEDROOMS",
            "replace": "4"
        },
        {
            "find": "BATHROOMS",
            "replace": "2"
        },
        {
            "find": "CARPORTS",
            "replace": "1"
        },
        {
            "find": "TYPE",
            "replace": "AUCTION"
        },
        {
            "find": "IMAGE_1",
            "replace": "https://shotstack-assets.s3.ap-southeast-2.amazonaws.com/images/realestate1.jpg"
        },
        {
            "find": "IMAGE_2",
            "replace": "https://shotstack-assets.s3.ap-southeast-2.amazonaws.com/images/realestate2.jpg"
        },
        {
            "find": "IMAGE_3",
            "replace": "https://shotstack-assets.s3.ap-southeast-2.amazonaws.com/images/realestate3.jpg"
        },
        {
            "find": "IMAGE_4",
            "replace": "https://shotstack-assets.s3.ap-southeast-2.amazonaws.com/images/realestate4.jpg"
        },
        {
            "find": "IMAGE_5",
            "replace": "https://shotstack-assets.s3.ap-southeast-2.amazonaws.com/images/realestate5.jpg"
        },
        {
            "find": "AGENT_PICTURE",
            "replace": "https://shotstack-assets.s3-ap-southeast-2.amazonaws.com/images/real-estate-agent-male.jpg"
        },
        {
            "find": "AGENT_NAME",
            "replace": "JEREMY SIMPSON"
        },
        {
            "find": "AGENT_EMAIL",
            "replace": "jeremy@blockrealestate.co"
        },
        {
            "find": "AGENCY_LOGO",
            "replace": "https://shotstack-assets.s3-ap-southeast-2.amazonaws.com/logos/real-estate-white.png"
        }
    ]
});

const config = {
    method: 'post',
    url: 'https://api.shotstack.io/v1/templates/render',
    headers: {
        'content-type': 'application/json',
        'x-api-key': 'rLzn3HLl6ENCy1dGCCNooL7EJAMyV8a9Qm2PEz2i'
    },
    data: data
};

axios(config)
    .then(function (response) {
        console.log(JSON.stringify(response.data, null, 2));
    })
    .catch(function (error) {
        console.log(error);
    });