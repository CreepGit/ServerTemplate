
async function ApiCall(url: string, callback: CallableFunction) {
    const value = await fetch(url)
        .then((response) => {
            if (response.status != 200) {
                return null
            }
            return response.json()
        })
    if (value == null)
        return console.log("Aborted")
    callback(value)
}

export { ApiCall }
