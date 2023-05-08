play = (e) => {
  console.log(e);
  const audio = document.querySelector(`audio[data-press="${e.keyCode}"]`);

  const key = document.querySelector(`li[data-press="${e.keyCode}"]`);

  if (audio) {
    audio.play();
    key.classList.add("play");
  }
};

pause = (e) => {
  console.log(e);
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);

  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);

  if (audio) {
    audio.currentTime = 0;
    audio.pause();

    key.classList.remove("play");
  }
};

// 4. 키보드를 눌렀을때 play함수가 실행되게, 키보드를 뗀다면 pause함수가 실행되게 해주세요.
//HINT: 전역객체 window와 addEventListener를 사용하세요.

window.addEventListener("keypress", play);
window.addEventListener("keyup", pause);
