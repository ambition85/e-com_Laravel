@extends('layouts.layout')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-xl-6">
            <img src="{{ asset($product->gallery) }}" alt="This is product image." class="detail-img">
        </div>
        <div class="col-xl-6">
            <a href="/">Go Back</a>
            <h2>{{$product->name}}</h2>
            <h3>Price : {{$product->price}}</h3>
            <h4>Detail : {{$product->description}}</h4>
            <h4>Category : {{$product->category}}</h4>
            <br><br>
            <button class="btn btn-primary">Add to Cart</button>
            <br><br>
            <button class="btn btn-success">Buy Now</button>
            <br><br>
        </div>
    </div>
</div>

@endsection


