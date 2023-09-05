<?php

namespace App\Http\Controllers;

use App\Products;
use App\Cart;
use Illuminate\Http\Request;
// use App\Http\Controllers\Auth;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
        $products = Products::all();
        return view('products.index', compact('products'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Products  $products
     * @return \Illuminate\Http\Response
     */
    public function show(Products $products)
    {
        //
        return view('products.show', compact('products'));
        // return $products;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Products  $products
     * @return \Illuminate\Http\Response
     */
    public function edit(Products $products)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Products  $products
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Products $products)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Products  $products
     * @return \Illuminate\Http\Response
     */
    public function destroy(Products $products)
    {
        //
    }

    public function detail($id){
        $product =  Products::find($id);
        return view('products.show', compact('product'));
        // return "sdfasdf";
    }

    public function addToCart(Request $req){
        // Check if user is logged in
        if (!Auth::check()) {
            return redirect()->route('login'); // Redirect to login page
        }
        $cart = new Cart;
        $cart->user_id = Auth::id();
        $cart->product_id = $req->product_id;
        $cart->save();
        return redirect('/')->with('success', "The product is added to the cart successfully!"); // Display "hello" message if user is logged in;
    }

    public static function cartItem(){
        $count = Cart::where('user_id', Auth::id())->count();
        return $count;
    }

    public function cartList(){
        $user_id = Auth::id();
        $products = DB::table('cart')
        ->join('products', 'cart.product_id', '=', 'products.id')
        ->where('cart.user_id', $user_id)
        ->select('products.*', 'cart.id as cart_id')
        ->get();

        return view('products.cartlist', compact('products'));
    }

    public function removeCart($id){
        Cart::destroy($id);
        return redirect('/cartlist');
    }

    public function orderNow(){
        $user_id = Auth::id();
        $products = Cart::join('products', 'cart.product_id', '=', 'products.id')
            ->where('cart.user_id', $user_id)
            ->select('products.*')
            ->get();

        $totalAmount = Cart::join('products', 'cart.product_id', '=', 'products.id')
        ->where('cart.user_id', $user_id)
        ->sum('products.price');
    
        $productInfo = [];

        foreach ($products as $product) {
            $name = $product['name'];
            $count = isset($productInfo[$name]['count']) ? $productInfo[$name]['count'] + 1 : 1;
            $pricePerPiece = $product['price'];
            $totalPrice = $count * $pricePerPiece;
            $productImage = $product->gallery;
            
            $productInfo[$name] = [
                'count' => $count,
                'price_per_piece' => $pricePerPiece,
                'total_price' => $totalPrice,
                'product_image' => $productImage
            ];
        }

        return view('products.ordernow', compact('productInfo', 'totalAmount'));
    }
}
