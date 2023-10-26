document.addEventListener("scroll", function () {
	var header = document.getElementById("header");
	if (window.scrollY > 0) {
	  header.classList.add("header-scrolled");
	} else {
	  header.classList.remove("header-scrolled");
	}
  });

  function rate(rating, blog_id) {
    fetch(`/rate/${blog_id}/${rating}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
            
        }
        throw new Error('Network response was not ok.');
    }).then(rest => {
        window.location.reload();
    }).catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

function highlightStars(rating) {
    const stars = document.querySelectorAll('.rating-list li i');
    stars.forEach((star, index) => {
        if (index < rating) {
            star.classList.add('checked');
        } else {
            star.classList.remove('checked');
        }
    });
}

function resetStars(user_rating) {
    const stars = document.querySelectorAll('.rating-list li i');
    stars.forEach((star, index) => {
        star.classList.toggle('checked', index < user_rating);
    });
}




