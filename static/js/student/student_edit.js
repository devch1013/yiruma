const card_number = document.querySelector("#id_card_number");
const card_bank = document.querySelector("#id_card_bank");

function changeSelect() {
  var selectedMethod = document.getElementById("id_payment_method"); // select element에서 선택된 option의 value가 저장된다.
  var selectValue = selectedMethod.options[selectedMethod.selectedIndex]; // select element에서 선택된 option의 text가 저장된다.
  if (selectValue.innerText != "카드결제") {
    card_number.parentElement.setAttribute("style", "display:none;");
    card_bank.parentElement.setAttribute("style", "display:none;");
  } else {
    card_number.parentElement.removeAttribute("style");
    card_bank.parentElement.removeAttribute("style");
  }
  console.log(typeof selectValue.innerText);
}
changeSelect();
