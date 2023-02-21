
function ApiGet(url: string) {
    return new Promise<any>((resolve, reject) => {
        fetch(url, {
            method: "GET",
        })
        .then(async response => {
            if (response.ok) {
                resolve(response.json())
            } else {
                console.log("This is not good :(")
                reject("Got the wrong response code")
            }
        })
    })
}

export { ApiGet }
