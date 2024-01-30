document.getElementById('checkButton').addEventListener('click', async function() {
    const text1 = document.getElementById('text1').value;
    const text2 = document.getElementById('text2').value;

    const response = await fetch('/check_plagiarism', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text1, text2 })
    });

    const data = await response.json();
    const resultElement = document.getElementById('result');
    resultElement.innerText = `Similarity: ${data.similarity.toFixed(2)}%`;
});
