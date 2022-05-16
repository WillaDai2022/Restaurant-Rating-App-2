function choose(items) {
    var index = Math.floor(Math.random() * items.length);
    return items[index];
  }


const get_recommended_rests = (qString) =>{

    fetch('/get_restaurants.json' + qString)
    .then(response => response.json())
    .then(responseData => {
      const data = responseData.businesses; 
    const recommend_container = document.querySelector('#recommend-rests');
    recommend_container.innerHTML = '';

    const rest1 = choose(data);
    const imgUrl1 = rest1.image_url;
    const city1= rest1.location.city; 
    const name1=rest1.name;
    if (!rest1.price){
      rest1.price = "$-$$$$"
    }

    console.log(rest1)

    const rest2 = choose(data);
    while(rest2 === rest1){
      rest2 = choose(data);
    }
      
    const imgUrl2 = rest2.image_url;
    const city2= rest2.location.city; 
    const name2=rest2.name;
    if (!rest2.price){
      rest2.price = "$-$$$$"
    }

   
    recommend_container.insertAdjacentHTML('beforeend',
      `<div class="col-md-3">
          <a class="rest-box" href="/rest_details/${rest1.id}" >
            <div>
              <img class="rest-image" src="${imgUrl1}" width="215px" height="190"/>
              <div>${name1}</div>
              <div class="price">${rest1.price}</div>
            </div>
          </a>
        </div>`)

    
    recommend_container.insertAdjacentHTML('beforeend',
      `<div class="col-md-3">
          <a class="rest-box" href="/rest_details/${rest2.id}" >
            <div>
              <img class="rest-image" src="${imgUrl2}" width="215px" height="190"/>
              <div>${name2}</div>
              <div class="price">${rest2.price}</div>
            </div>
          </a>
        </div>`)
    })
}

const restLocation = document.querySelector("#recommend-rests").getAttribute("data-location");
console.log(restLocation)
get_recommended_rests(`?location=${restLocation}`);