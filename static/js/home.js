showAllRests(""); 


document.querySelector('#where-to').addEventListener('submit', (evt)  => {
    evt.preventDefault(); // Prevent the submision of the form
    showAllRests(`?location=${evt.target.querySelector("input").value}`); // Fetch the data
  });