show_all_rests(""); 


document.querySelector('#where-to').addEventListener('submit', (evt)  => {
    evt.preventDefault(); // Prevent the submision of the form
    show_all_rests(`?location=${evt.target.querySelector("input").value}`); // Fetch the data
  });