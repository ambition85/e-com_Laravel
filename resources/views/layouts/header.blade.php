<?php
  use App\Http\Controllers\ProductController;
  $count = ProductController::cartItem();
?>

<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="/">Logo</a>
  <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navb">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navb">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="javascript:void(0)">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="javascript:void(0)">Orders</a>
      </li>
        <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="text" placeholder="Search">
            <button class="btn btn-success my-2 my-sm-0" type="button">Search</button>
        </form>
      </li>
    </ul>

    <ul class="navbar-nav navbar-right">
        <li class="nav-item">
            <a class="nav-link" href="javascript:void(0)">Cart({{ $count }})</a>
        </li>
    </ul>

  </div>
</nav>