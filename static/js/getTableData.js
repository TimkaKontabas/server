const selectTable = document.getElementById('select_tables');
const table = document.getElementById('table');


selectTable.addEventListener('change', (event) => {
    const table = event.target.value;
    const text = event.target.options[event.target.selectedIndex].text;
    let data = {
        table: text
    };
    fetch('/get_table', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Обработка полученных данных
        console.log(data);
        console.log(data.data);
    })
    .catch(error => {
        // Обработка ошибок
        console.error(error);
    });
})