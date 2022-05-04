
const button = document.querySelector('#fav-rest')
button.addEventListener('click', (evt)=> {
  evt.preventDefault();

    const restInfo = {
        name: button.dataset.name,
        address1: button.dataset.address1,
        address2: button.dataset.address2,
        url: button.dataset.url,
        yelp_id: button.dataset.yelp,
      };

      fetch('/add_fav_rest', {
        method: 'POST',
        body: JSON.stringify(restInfo),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => response.json())
        .then(responseJson => {
          alert(responseJson.status);

          //TODO Udate nav-bar favorites 
        });
    });


