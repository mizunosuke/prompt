const form = document.getElementById("animal-form");
const resultDiv = document.getElementById("result");
const st = io.connect("http://" + document.domain + ":" + location.port);

let responses = [];
let isResponseFinished = false;

function add1(){
  document.getElementById('message').value='パスワードがわかりません';
  }
function add2(){
  document.getElementById('message').value='配送された商品の大きさが違っていました。返品できますか？';
  }
function add3(){
  document.getElementById('message').value='商品が届きません！';
  }
function add4(){
  document.getElementById('message').value='商品のラッピングについてききたいです';
  }
function add5(){
  document.getElementById('message').value='メールが届きません';
  }

function activateUrls(text) {
  const urlRegex = /(https?:\/\/[^\s]+)/g;
  return text.replace(urlRegex, (url) => `<a href="${url}" target="_blank" class="font-medium text-blue-600 hover:underline">${url}</a>`);
}

st.on("response", (data) => {
  const parsedData = JSON.parse(data);

  if (parsedData.answer.content) {
    resultDiv.innerHTML += parsedData.answer.content;
    responses.push(parsedData.answer.content);
  } else {
    const combinedText = responses.join("");
    const textWithActivatedUrls = activateUrls(combinedText);
    resultDiv.innerHTML = textWithActivatedUrls;
  }
});

form.addEventListener("submit", (event) => {
  resultDiv.innerHTML = "";
  responses = [];
  isResponseFinished = false;
  event.preventDefault();
  const formData = new FormData(form);
  const animal = formData.get("animal");

  st.emit("message", { animal: animal });
});
