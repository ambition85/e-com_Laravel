@extends('layouts.layout')

@section('content')
<div class="container">         
  <table class="table table-bordered bill-table">
    <thead>
      <tr>
        <th>Product</th>
        <th>Count</th>
        <th>Price per Piece</th>
        <th>Price</th>
      </tr>
    </thead>
    <tbody>
        @foreach ($productInfo as $name=>$info)
        <tr>
            <td><img class="td-prodcut-image" src="{{$info['product_image']}}" alt="">   {{$name}}</td>
            <td>{{$info['count']}}</td>
            <td>{{$info['price_per_piece']}}</td>
            <td>{{$info['total_price']}}</td>
        </tr>
        @endforeach
    </tbody>
  </table>
  <h3 class="total_price">Total Price : {{$totalAmount}}</h3><br><br>
  <form action="">
        <textarea type="text" name="address" class="address_textarea" placeholder="Input your address"></textarea><br><br>
        <p><strong>Payment method</strong></p>
        <input type="radio" name="payment"><span>online payment</span><br><br>
        <input type="radio" name="payment"><span>EMI payment</span><br><br>
        <input type="radio" name="payment"><span>Payment on Delivery</span><br><br>
        <button class="btn btn-primary" type="submit">Order Now</button>
  </form>

</div>
<!-- @foreach ($productInfo as $name => $info)
    <p>name: {{$name}} count: {{$info['count']}} price_per_piece: {{$info['price_per_piece']}} total_price: {{$info['total_price']}}</p>
@endforeach -->
@endsection