const noButton = document.querySelectorAll('.del-rest');


for (const button of noButton){ 
  button.addEventListener('click', (evt)=> {
    evt.preventDefault();
    
      fetch('/delete_fav_rest', {
        method: 'POST',
        body: JSON.stringify({
          "yelp_id": evt.currentTarget.value,
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => response.json())
        .then(responseJson => {
          location.reload(true)
        });
    });

}