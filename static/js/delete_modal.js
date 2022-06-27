const modal_title = document.querySelector(".modal-title");
const modal_body = document.querySelector(".modal-body");
const delete_button = document.querySelector(".btn-default");

function reply_click(obj) {
  modal_title.innerText = obj.id;
  modal_body.innerText =
    obj.value +
    " 학생의 데이터를 삭제하시겠습니까?" +
    "\n학생의 결제 데이터도 모두 삭제됩니다." +
    "\n데이터는 복구할 수 없습니다";
  delete_button.setAttribute("value", obj.id);
  console.log("hello");
}
