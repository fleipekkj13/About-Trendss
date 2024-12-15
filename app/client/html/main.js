function pesquisar() {
    fetch('https://fb3f-186-224-160-24.ngrok-free.app/search', {
        method: 'get',
        headers: {
            'ngrok-skip-browser-warning': '9992'
        }
    }).then((res) => {
        console.log(res.json().then((res) => {
            console.log(typeof(res));
        }))
    })
}