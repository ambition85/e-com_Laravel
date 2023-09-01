<?php

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class ProductSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //
        DB::table('products')->insert([
            [
                'name' => "Opoo mobile",
                'price' => "300",
                'description' => "A smartphone with 8GB ram and much more features",
                'category' => "mobile",
                'gallery' => "images/oppo_mobile.jpg"
            ],
            [
                'name' => "LG mobile",
                'price' => "200",
                'description' => "A smartphone with 4GB ram and much more features",
                'category' => "mobile",
                'gallery' => "images/lg_mobile.jpg"
            ],
            [
                'name' => "Panasonic TV",
                'price' => "400",
                'description' => "A smartTV with much more features",
                'category' => "tv",
                'gallery' => "images/panasonic_tv.jpg"
            ],
            [
                'name' => "SONY TV",
                'price' => "500",
                'description' => "A TV with much more features",
                'category' => "tv",
                'gallery' => "images/sony_tv.jpg"
            ],
            [
                'name' => "LG Fridge",
                'price' => "200",
                'description' => "A fridge with much more features",
                'category' => "fridge",
                'gallery' => "images/lg_fridge.jpg"
            ],
    ]);
    }
}
