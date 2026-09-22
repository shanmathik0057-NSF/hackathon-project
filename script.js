* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #f4f7fb;
    color: #172033;
    line-height: 1.6;
}

header {
    background: #111827;
    color: white;
    padding: 35px 8%;
    text-align: center;
}

header h1 {
    font-size: 42px;
    letter-spacing: 3px;
    margin-bottom: 8px;
}

header p {
    font-size: 16px;
    color: #cbd5e1;
}

main {
    width: 90%;
    max-width: 1100px;
    margin: 35px auto;
    display: grid;
    gap: 25px;
}

section {
    background: white;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

section h2 {
    margin-bottom: 15px;
    font-size: 22px;
}

.failure {
    border-left: 6px solid #ef4444;
}

.failure h3 {
    font-size: 25px;
    margin-bottom: 8px;
}

ul,
ol {
    padding-left: 25px;
}

li {
    margin: 8px 0;
}

.chain {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.chain div {
    background: #eef2ff;
    padding: 14px 20px;
    border-radius: 10px;
    font-weight: bold;
}

.chain span {
    font-size: 24px;
    font-weight: bold;
}

@media (max-width: 700px) {
    header h1 {
        font-size: 32px;
    }

    .chain {
        flex-direction: column;
    }

    .chain span {
        transform: rotate(0deg);
    }
}
