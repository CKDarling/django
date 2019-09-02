var restart = document.querySelector('#boy')
var squares = document.querySelectorAll('td')

// clear Board //
function clearBoard(){
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
    }
};
restart.addEventListener('click',clearBoard)

// X or O Creator
function symbolCreator(){
  if (this.textContent === ''){
    this.textContent = 'X';
  }else if (this.textContent ==='X') {
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
};
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',symbolCreator);
}
