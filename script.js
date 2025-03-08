document.getElementById('environmentalForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const formData = {
        temp: parseFloat(document.getElementById('temp').value),
        rainfall: parseFloat(document.getElementById('rainfall').value),
        ph: parseFloat(document.getElementById('ph').value),
        dissolvedOxygen: parseFloat(document.getElementById('dissolvedOxygen').value)
    };

    fetch('http://127.0.0.1:5000/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        document.getElementById('result').textContent = `Predicted Water Level: ${data.predicted_water_level} m`;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error: Could not connect to the server. Ensure it is running.');
        document.getElementById('result').textContent = '';
    });
});