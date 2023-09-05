@extends('layouts.layout')

@section('content')
<div class="container">
    <div class="row">
        <h1>Cart</h1>
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
            <button class="btn btn-warning">Remove from Cart</button>
        </div>
    </div>
    @endforeach
</div>
@endsection