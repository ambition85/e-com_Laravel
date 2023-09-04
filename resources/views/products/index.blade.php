@extends('layouts.layout')

@section('content')

@if($message = Session::get('success'))
<div class="alert alert-success alert-dismissible fade show">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    <p>{{ $message }}</p>
  </div>
@endif

    <div id="demo" class="carousel slide custom-product" data-ride="carousel">
        <ul class="carousel-indicators">
            @foreach ($products as $product)
            <li data-target="#demo" data-slide-to="{{ $product->id-1 }}" class="{{$product->id==1 ? 'active' : ''}}"></li>
            @endforeach
        </ul>
        <div class="carousel-inner">
            @foreach ($products as $product)
            <div class="carousel-item {{$product->id==1 ? 'active' : ''}}">
                <a href="detail/{{$product->id}}">
                    <img class="slider-img" src="{{$product->gallery}}">
                    <div class="carousel-caption slider-text">
                        <h3>{{ $product->name }}</h3>
                        <p>{{ $product->description}}</p>
                    </div>  
                </a> 
            </div>
            @endforeach
        </div>
        <a class="carousel-control-prev prev-icon" href="#demo" data-slide="prev">
            <span class="carousel-control-prev-icon"></span>
        </a>
        <a class="carousel-control-next next-icon" href="#demo" data-slide="next">
            <span class="carousel-control-next-icon"></span>
        </a>
    </div>

    <div class="trending-wrapper">
        <h3>Trending Products</h3>
        @foreach ($products as $product)
            <div class="trending-item">                    
                <a href="/detail/{{ $product->id }}">
                    <img class="trending-image" src="{{$product->gallery}}">
                    <div class="">
                        <h4>{{ $product->name }}</h3>
                    </div> 
                </a>  
            </div>

        @endforeach
    </div>
@endsection