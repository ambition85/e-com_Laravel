<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Auth::routes();

Route::get('/home', 'HomeController@index')->name('home');

Route::get('/', 'ProductController@index');
Route::post('add_to_cart', "ProductController@addToCart");
Route::get('detail/{id}', 'ProductController@detail');
Route::get('cartlist', "ProductController@cartList");
Route::get('removecart/{id}', "ProductController@removeCart");
Route::get('ordernow', "ProductController@orderNow");


// Route::group(['middleware' => ['auth']], function() {
// });

// Route::get('/', function () {
//     return view('welcome');
// });


