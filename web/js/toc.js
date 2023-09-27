function build_toc() {
   toc_div = document.getElementById("table-of-contents");
   toc_items = Array.from(document.getElementsByClassName("toc-section"));
   toc_ls = document.createElement("ol");
   
   toc_items.map((el) => {
      toc_bullet = document.createElement("li");
      toc_item = document.createElement("a");
      toc_item.innerHTML = el.parentNode.nextElementSibling.innerHTML;
      toc_item.href = "#" + el.id;
      toc_bullet.appendChild(toc_item);
      toc_ls.appendChild(toc_bullet);
   });
   toc_div.appendChild(toc_ls);
}

build_toc();
