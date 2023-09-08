@extends('layouts.layout')

@section('content')
@foreach($searchedProducts as $product)
<p>{{$product->name}}</p>
<img src="{{$product->gallery}}" alt="">
@endforeach
@endsection