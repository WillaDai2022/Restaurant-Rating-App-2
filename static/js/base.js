
const show_all_rests = (q_string) => {

  fetch('/get_restaurants.json' + q_string)
  .then(response => response.json())
  .then(responseData => {

    const data = responseData.businesses;
    const rest_container = document.querySelector('#listing-grids');
    
    rest_container.innerHTML = '';
    
    for(const rest of data){
      imgUrl = rest.image_url;
      city= rest.location.city; 
      name=rest.name;

      rest_container.insertAdjacentHTML('beforeend',
      `<div>
        <div>Restaurants in ${city}</div>
        <a href="/rest_details/${rest.id}" >
          <div class="restaurant-box">
            <img src="${imgUrl}" width="200" height="200" />
            <div>${name}</div>
            <div>${rest.price}</div>
          </div>
        </a>
      </div>`)
    };
  });
}

document.querySelector('#nav-where-to').addEventListener('submit', (evt)  => {
      evt.preventDefault(); // Prevent the submision of the form
      show_all_rests(`?location=${evt.target.querySelector("input").value}`)
    });



// document.querySelector('#nav-where-to').addEventListener('submit', (evt)  => {
//     evt.preventDefault(); // Prevent the submision of the form
//     window.location.replace(`/?location=${evt.target.querySelector("input").value}`)
//   });


// function getQueryVariable(variable){
//   let query = window.location.search.substring(1);
//   let vars = query.split("&");
//   for (let i=0;i<vars.length;i++) {
//           let pair = vars[i].split("=");
//           if(pair[0] == variable){return pair[1];}
//   }
//   return(false);
// }

// queryString = getQueryVariable("location")

// document.querySelector('#nav-where-to').addEventListener('submit', (evt)  => {
//   evt.preventDefault(); // Prevent the submision of the form
//   show_all_rests(`/?location=${queryString}`)
// });