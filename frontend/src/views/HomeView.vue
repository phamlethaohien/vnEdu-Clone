<template>
  <div class="home">
    <div>
      <b-carousel controls indicators style="text-shadow: 1px 1px 2px #333;" @sliding-start="onSlideStart" @sliding-end="onSlideEnd">
        <b-carousel-slide img-src="https://firebasestorage.googleapis.com/v0/b/vneduclone.appspot.com/o/home_carousel_3.png?alt=media&token=3fd63468-65eb-4c10-a577-2289ccca5f5c&_gl=1*10p8okv*_ga*MTUxNjQyNzAxMS4xNjg2NTM5NDM0*_ga_CW55HF8NVT*MTY4NjUzOTQzNC4xLjEuMTY4NjUzOTc2My4wLjAuMA.." ></b-carousel-slide>

        <b-carousel-slide img-src="https://firebasestorage.googleapis.com/v0/b/vneduclone.appspot.com/o/home_carousel_1.png?alt=media&token=b41b49be-531b-4d06-a3ba-0ee0e0a8a320&_gl=1*vvervz*_ga*MTUxNjQyNzAxMS4xNjg2NTM5NDM0*_ga_CW55HF8NVT*MTY4NjUzOTQzNC4xLjEuMTY4NjUzOTczNC4wLjAuMA..">
        </b-carousel-slide>

        <b-carousel-slide img-src="https://firebasestorage.googleapis.com/v0/b/vneduclone.appspot.com/o/home_carousel_2.png?alt=media&token=8cd7d84c-27ac-4ac8-8879-3724d17f5fc6&_gl=1*hp5322*_ga*MTUxNjQyNzAxMS4xNjg2NTM5NDM0*_ga_CW55HF8NVT*MTY4NjUzOTQzNC4xLjEuMTY4NjUzOTc0Ny4wLjAuMA.."></b-carousel-slide>
      </b-carousel>
    </div>

    <div class="service-card py-5">
      <div class="container">
        <div class="row g-4">
          <div class="col-lg-3 col-sm-6 wow fadeInUp" data-wow-delay="0.1s">
            <div class="service-item text-center pt-3">
              <div class="p-4">
                <i class="fa fa-3x fa-graduation-cap service_icon mb-4"></i>
                <h5 class="mb-3 fw-medium">Skilled Instructors</h5>
                <p>Diam elitr kasd sed at elitr sed ipsum justo dolor sed clita amet diam</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-sm-6">
            <div class="service-item text-center pt-3">
              <div class="p-4">
                <i class="fa fa-3x fa-globe service_icon mb-4"></i>
                <h5 class="mb-3 fw-medium">Online Classes</h5>
                <p>Diam elitr kasd sed at elitr sed ipsum justo dolor sed clita amet diam</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-sm-6">
            <div class="service-item text-center pt-3">
              <div class="p-4">
                <i class="fa fa-3x fa-home service_icon mb-4"></i>
                <h5 class="mb-3 fw-medium">Home Projects</h5>
                <p>Diam elitr kasd sed at elitr sed ipsum justo dolor sed clita amet diam</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-sm-6">
            <div class="service-item text-center pt-3">
              <div class="p-4">
                <i class="fa fa-3x fa-book-open service_icon mb-4"></i>
                <h5 class="mb-3 fw-medium">Book Library</h5>
                <p>Diam elitr kasd sed at elitr sed ipsum justo dolor sed clita amet diam</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.service-item {
    background: var(--light);
    transition: .5s;
}

.service-item:hover {
    margin-top: -10px;
    background: var(--primary);
}

.service-item * {
    transition: .5s;
}
.service_icon {
  color: #06BBCC !important;
}

.service-item:hover * {
    color: var(--light) !important;
}


</style>
