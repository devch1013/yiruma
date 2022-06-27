const query = new URL(window.location.href);
const params = new URLSearchParams(query.search);

const today = new Date();
const current_month =
  today.getFullYear() +
  "-" +
  ("0" + (today.getMonth() + 1).toString()).slice(-2);

const temp_input = document.querySelector("#temp_input");

const month = document.querySelector("#month");
const all_button = document.querySelector("#all");
const current_button = document.querySelector("#current");

const make_db = document.querySelector("#make_db");

const q = query.searchParams.get("q");
const month_value = query.searchParams.get("month");
// console.log(query.searchParams.get("q"));
all_button.setAttribute("onclick", `window.location="/fin/?q=${q}";`);
current_button.setAttribute(
  "onclick",
  `window.location="/fin/?q=${q}&month=${current_month}";`
);
console.log(current_button.innerText);
temp_input.setAttribute("value", q);
month.setAttribute("value", month_value);
make_db.setAttribute("value", month_value);
if (month_value == null || month_value == "") {
  make_db.setAttribute("style", "display:none;");
}
make_db.innerText = `${month_value} 의 결제 목록 만들기`;
