const today = new Date();
const current_month =
  today.getFullYear() +
  "-" +
  ("0" + (today.getMonth() + 1).toString()).slice(-2);

const money_link1 = document.querySelector("a.money-link1");
const money_link2 = document.querySelector("a.money-link2");
const money_link3 = document.querySelector("a.money-link3");
money_link1.setAttribute("href", money_link1.href + "?month=" + current_month);
money_link2.setAttribute("href", money_link2.href + "&month=" + current_month);
money_link3.setAttribute("href", money_link3.href + "&month=" + current_month);
