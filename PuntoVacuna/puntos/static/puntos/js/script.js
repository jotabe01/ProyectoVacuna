//API VOICE CONTACTO
const iniciarG = document.getElementById('iniciarG')
const detenerG = document.getElementById('detenerG')
const texto = document.getElementById('com')

let recognition = new webkitSpeechRecognition();
recognition.lang ='es-AR';
recognition.continuous = true;
recognition.interimResoults = true;

recognition.onresult = (event)=>{
    const results = event.results;
    const frase = results[results.length-1][0].transcript;
    texto.value += frase;
}
iniciarG.addEventListener('click',()=>{
    recognition.start();
});
detenerG.addEventListener('click',()=>{
    recognition.stop();
});

