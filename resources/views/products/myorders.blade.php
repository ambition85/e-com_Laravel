@extends('layouts/layout')

@section('content')
@foreach ($myorders as $myorder)
<img src="{{$myorder->gallery}}" alt="">
@endforeach
@endsection