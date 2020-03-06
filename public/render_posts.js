class Item {
  constructor(name) {
    this.name = name
  }
}

class UI {
  createItem(item) {
    const list = document.getElementById("list")

    // Create element
    const row = document.createElement('div');
    row.className = "container"
    row.innerHTML =`
      <p>${item.name}</p>
    `;

    // list.appendChild(row);
    list.insertBefore(row, list.childNodes[0])
  }

  clearFields() {
    document.getElementById('item').value = ''
  }
}



// Event listener for add book
document.getElementById('input').addEventListener('submit',
(e) => {
  // Get form values
  const name = document.getElementById('item').value
  const item = new Item(name);
  const ui = new UI();
  ui.createItem(item);
  ui.clearFields();

  e.preventDefault();
})