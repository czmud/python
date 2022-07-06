let username = 'bryankenote';

async function getCoderData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/"+username);
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    console.log(coderData);
    console.log(coderData.avatar_url)
    return coderData;
}


