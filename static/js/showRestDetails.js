// let data=""

// Get url variable
// function getQueryVariable(variable)
// {
//        const query = window.location.search.substring(1);
//        const vars = query.split("&");
//        for (let i=0;i<vars.length;i++) {
//                const pair = vars[i].split("=");
//                if(pair[0] == variable){return pair[1];}
//        }
//        return(false);
// }
// yelp_id = getQueryVariable("id")






// Show restaurant details
// const show_a_rests = () => {
//     const rest_container = document.querySelector('#rest-info');

  
//     fetch(`/get_rest_details/${yelp_id}`)
//     .then(response => response.json())
//     .then(responseData => {
//         rest = responseData;
//         url=rest.image_url;
//         city= rest.location.city;
        
      
//         rest_container.innerHTML=
//         `<div>
//               <div>Restaurants in ${city}</div>
//               <img class="detai-image" src=${url}>
//               <div class="detail-name">${rest.name}</div>
//               <div>Phone: ${rest.display_phone}</div>
//               <div>Address: ${rest.location.display_address}</div>
//               <p>What people are saying</p>
//             </div>
//         `});
//        }
  
// show_a_rests();

// // Show restaurant reviews
// const show_reviews = () => {
//   const rest_container = document.querySelector('#rest-reviews');

//   fetch(`/get_rest_review/${yelp_id}`)
//   .then(response => response.json())
//   .then(responseData => {
//     data = responseData
//      if(responseData.length == 0){

//        for(const review of responseData){
//         rest_container.insertAdjacentHTML("beforeend", 
//         `<div>
//           ${review.title}
//         </div>`
//         )
//        }
//       }else{
//         rest_container.innerHTML = "No review yet";
//       }
//   });
// }
  
// show_reviews();


// //Customer click to leave a review
// document.querySelector('#review-button').addEventListener('click', ()  => {
//   window.location.href="/review_page/${yelp_id}"
// });



const lat = Number(document.querySelector('#map').getAttribute('data-lat'))
const lng = Number(document.querySelector('#map').getAttribute('data-lng'))

function initMap(){
    
    var options = {
        zoom: 12,
        center:{lat:lat, lng:lng}
    }

    var map = new google.maps.Map(
        document.getElementById('map'), options);

    var marker = new google.maps.Marker({
        position:{lat:lat, lng:lng},
        map:map, 
    });
}
