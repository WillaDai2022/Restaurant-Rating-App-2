
const show_all_rests = (q_string) => {

  let data = ''
  let randRest=''

  fetch('/get_restaurants.json' + q_string)
  .then(response => response.json())
  .then(responseData => {

    const data = responseData.businesses; // need to handel getting a invalid response 
    const rest_container = document.querySelector('#listing-grids');
    
    rest_container.innerHTML = '';
    
    for(const rest of data){
      imgUrl = rest.image_url;
      city= rest.location.city; 
      name=rest.name;

      rest_container.insertAdjacentHTML('beforeend',
      `<div class="col-md-3">
          <a class="rest-box" href="/rest_details/${rest.id}" >
            <div>
              <img class="rest-image" src="${imgUrl}" width="215px" height="190"/>
              <div>${name}</div>
              <div class="price">${rest.price}</div>
            </div>
          </a>
        </div>`)
    };
  
    // console.log('data: ', data)
  const rand = Math.floor(Math.random()*data.length);
  // console.log('rand: ', rand)
  randRest = data[rand];
  
  // console.log(document.querySelector('.test'))

  const test = document.createElement('div');
  //add hidden attribute so it hides this
  //then create button with event listener for random rest
  //if user clicks that button, remove the hidden attribute to show this restaurant
  test.innerHTML = `&&&&&&&&&&&&&&&&& ${randRest.name}`
  document.querySelector('.test').appendChild(test)

  });
}

document.querySelector('#nav-where-to').addEventListener('submit', (evt)  => {
      evt.preventDefault(); // Prevent the submision of the form
      let randRest = show_all_rests(`?location=${evt.target.querySelector("input").value}`)
      console.log(randRest);
      console.log("*******")
    });



