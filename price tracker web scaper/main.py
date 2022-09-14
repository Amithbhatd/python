import requests
from bs4 import BeautifulSoup


products_to_track = [
    {
        "product_URL": "https://www.amazon.in/Logitech-Hyperion-Ultra-Gaming-Mouse/dp/B00NFD0ETQ/ref=sr_1_10?crid=3HUN5D4V6RT0T&keywords=logitech&qid=1663139037&s=computers&sprefix=%2Ccomputers%2C178&sr=1-10",
        "name": "Logitech G402 Hyperion Fury USB Wired Gaming Mouse",
        "target_price": 2300
    },
    {
        "product_URL": "https://www.amazon.in/Callas-Multipurpose-Breakfast-Ergonomic-WA-27-Black/dp/B08MZQBFLN/ref=zg_bs_1458204031_sccl_11/262-6173989-8371742?pd_rd_i=B08MZQBFLN&th=1",
        "name": "Bed table",
        "target_price": 700
    },
    {
        "product_URL": "https://www.amazon.in/dp/B084DWH53T?ref_=nav_em_in_pc_sbc_BE_0_2_2_2",
        "name": "sad alexa",
        "target_price": 4200
    },
    {
        "product_URL": "https://www.amazon.in/dp/B00IP6C1AI/ref=s9_acsd_al_bw_c2_x_14_i?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-12&pf_rd_r=GVR3X22GVBQEX92ZQB62&pf_rd_t=101&pf_rd_p=68dcd57f-bc87-453a-85e7-8c68db795c7e&pf_rd_i=15358786031",
        "name" : "Extension cord",
        "target_price": 300

    },
    {
        "product_URL" : "https://www.amazon.in/E-tech-Power-Strip-4-1/dp/B07WNW4G39/ref=d_pb_allspark_purchase_sims_desktop_sccl_2_21/262-6173989-8371742?pd_rd_w=DOjV7&content-id=amzn1.sym.a4543507-b579-4aa3-8a29-824b6607c4d8&pf_rd_p=a4543507-b579-4aa3-8a29-824b6607c4d8&pf_rd_r=BZX0B348XNCX3F77EBV4&pd_rd_wg=SjAbf&pd_rd_r=8d1c294f-16a3-4a86-b6de-1a92896b5c47&pd_rd_i=B07WNW4G39&psc=1",
        "name" : "More plug Extension cord",
        "target_price": 800
    }

]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

    }
    page = requests.get(URL, headers=headers)

    broth = BeautifulSoup(page.content, 'html.parser')


    product_price = broth.find("span", class_="a-price-whole").text

    return product_price



result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_URL"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[0:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' - \t' + 'Available at Target Price' + ' current price - ' + str(my_product_price) + '\n')

        else:
            print("Still at current price")

finally:
    result_file.close()





