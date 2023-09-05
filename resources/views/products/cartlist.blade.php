@extends('layouts.layout')

@section('content')
<div class="container">
    <div class="row cart-title">
        <h1>Cart</h1>
        <a href="ordernow" class="btn btn-success">Order Now</a>
        <br><br>
    </div>    
    @foreach ($products as $product)
    <div class="row cart-list">
        <div class="col-sm-3">
            <img src="{{ $product->gallery }}" alt="product image" class="trending-image">
        </div>
        <div class="col-sm-4">
            <h3>{{$product->name}}</h3>
            <h4>${{$product->price}}</h4>
            <h4>{{$product->description}}</h4>
        </div>
        <div class="col-sm-4">
            <a href="/removecart/{{$product->cart_id}}" class="btn btn-warning">Remove from Cart</a>
        </div>
    </div>
    @endforeach
    <a href="ordernow" class="btn btn-success">Order Now</a>
</div>
@endsection