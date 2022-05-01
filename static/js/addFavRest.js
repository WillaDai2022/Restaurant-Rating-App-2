
const button = document.querySelector('#fav-rest')
button.addEventListener('click', ()=> {

    const restInfo = {
        name: button.getAttribute('data-name'),
        address1: button.getAttribute('data-address1'),
        address2: button.getAttribute('data-address2'),
        utl: button.getAttribute('data-url'),
        yelp_id: button.getAttribute('data-yelp')
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
        });
    });


