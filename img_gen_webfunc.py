import requests
import json
import base64

import cv2
import numpy as np
import os
import datetime


def cv2_to_base64(image):
    data = cv2.imencode('.jpg', image)[1]
    return base64.b64encode(data.tobytes()).decode('utf8')


def base64_to_cv2(b64str):
    data = base64.b64decode(b64str.encode('utf8'))
    data = np.frombuffer(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data


def get_resnet50_vd_animals(img_path='./images/animals.jpg'):
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/resnet50_vd_animals"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))

    # 打印预测结果
    res = r.json()["results"]
    return res


def get_openpose_body_estimation(img_path='./images/openpose/demo.jpg'):
    org_im = cv2.imread(img_path)
    data = {'images': [cv2_to_base64(org_im)]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/openpose_body_estimation"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    print(r.json())
    # canvas = base64_to_cv2(r.json()["results"]['data'])
    # savepath = os.path.abspath('.') + "\\" + "openpose_body_estimation_result"
    # # 不存在则创建
    # if not os.path.exists(savepath):
    #     os.makedirs(savepath)
    # output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    # cv2.imwrite(output_path, canvas)
    # return output_path


def get_chinese_ocr_db_crnn_server(img_path='./images/ocr/demo.jpg'):
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/chinese_ocr_db_crnn_server"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))

    # 打印预测结果
    # print(r.json())
    res = r.json()["results"]
    output_path = r.json()["results"][0]["save_path"]
    return res, output_path


def get_yolov3_resnet50_vd_coco2017(img_path='./images/animals.jpg'):
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/yolov3_resnet50_vd_coco2017"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # 打印预测结果
    res = r.json()["results"]
    output_path = r.json()["results"][0]["save_path"]
    return res, output_path


def get_stylepro_artistic(content_img_path='./images/demo1.jpg', style_img_path='./images/styles/style1.jpg'):
    # 发送HTTP请求
    data = {'images': [
        {
            'content': cv2_to_base64(cv2.imread(content_img_path)),
            'styles': [cv2_to_base64(cv2.imread(style_img_path))]
        }
    ]}

    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/stylepro_artistic"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    res = cv2.cvtColor(base64_to_cv2(r.json()["results"][0]['data']), cv2.COLOR_RGB2BGR)

    # 保存路径
    savepath = os.path.abspath('.') + "\\" + "stylepro_artistic_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, res)
    return output_path


def get_stgan_bald(img_path='./images/demo1.jpg'):
    img = cv2.imread(img_path)
    data = {'images': [cv2_to_base64(img)]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/stgan_bald"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(r.json())
    # 保存图片 1年 3年 5年
    one_year = cv2.cvtColor(base64_to_cv2(r.json()["results"]['data_0']), cv2.COLOR_RGB2BGR)
    three_year = cv2.cvtColor(base64_to_cv2(r.json()["results"]['data_1']), cv2.COLOR_RGB2BGR)
    five_year = cv2.cvtColor(base64_to_cv2(r.json()["results"]['data_2']), cv2.COLOR_RGB2BGR)
    # 保存路径
    savepath = os.path.abspath('.') + "\\" + "stgan_bald_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, five_year)
    return output_path


def get_animegan_v1_hayao_60(img_path='./images/demo1.jpg'):
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/animegan_v1_hayao_60"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # 打印预测结果
    print(r.json())
    img = base64_to_cv2(r.json()["results"][0])
    savepath = os.path.abspath('.') + "\\" + "animegan_v1_hayao_60_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, img)
    return output_path


def get_pyramidbox_lite_server_mask(img_path='./images/mask/demo.jpg'):
    # 发送HTTP请求
    data = {'images': [cv2_to_base64(cv2.imread(img_path))]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/pyramidbox_lite_server_mask"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))

    # 打印预测结果
    res = r.json()["results"][0]["data"]
    path = r.json()["results"][0]["path"]
    output_path = '.\pyramidbox_lite_server_mask_result' + '\\' + path + '.jpg'
    return res, output_path


def get_user_guided_colorization(img_path='./images/photo/demo.jpg'):
    # 发送HTTP请求
    org_im = cv2.imread(img_path)
    data = {'images': [cv2_to_base64(org_im)]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/user_guided_colorization"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    data = base64_to_cv2(r.json()["results"]['data'][0]['fake_reg'])

    savepath = os.path.abspath('.') + "\\" + "colorization_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, data)
    return output_path


def get_deoldify(img_path='./images/photo/demo.jpg'):
    # 发送HTTP请求
    org_im = cv2.imread(img_path)
    data = {'images': cv2_to_base64(org_im)}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/deoldify"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(r.json())
    img = base64_to_cv2(r.json()["results"])
    savepath = os.path.abspath('.') + "\\" + "deoldify_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, img)
    return output_path


def get_photo_restoration(img_path='./images/photo/demo.jpg'):
    # 发送HTTP请求
    org_im = cv2.imread(img_path)
    data = {'images': cv2_to_base64(org_im), 'model_select': ['Colorization']}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/photo_restoration"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(r.json())
    # 保存图片

    img = base64_to_cv2(r.json()["results"])
    savepath = os.path.abspath('.') + "\\" + "photo_restoration_result"
    # 不存在则创建
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
    cv2.imwrite(output_path, img)
    return output_path


def get_humanseg_server(img_path='./images/demo1.jpg'):
    # 发送HTTP请求
    org_im = cv2.imread(img_path)
    data = {'images': [cv2_to_base64(org_im)]}
    headers = {"Content-type": "application/json"}
    url = "http://127.0.0.1:8866/predict/humanseg_server"
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    output_path = ''
    if r:
        # 保存图片
        mask = cv2.cvtColor(base64_to_cv2(r.json()["results"][0]['data']), cv2.COLOR_BGR2GRAY)
        rgba = np.concatenate((org_im, np.expand_dims(mask, axis=2)), axis=2)
        savepath = os.path.abspath('.') + "\\" + "humanseg_server_result"
        # 不存在则创建
        if not os.path.exists(savepath):
            os.makedirs(savepath)
        output_path = savepath + "\\" + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.png'
        cv2.imwrite(output_path, rgba)
    return output_path


def main1():
    res = get_resnet50_vd_animals()
    print(res)
    print("Done!")


def main2():
    output_path = get_openpose_body_estimation()
    print(output_path)
    print("Done!")


def main3():
    res, output_path = get_chinese_ocr_db_crnn_server()
    print(res)
    print(output_path)
    print("Done!")


def main4():
    res, output_path = get_yolov3_resnet50_vd_coco2017()
    print(res)
    print(output_path)
    print("Done!")


def main5():
    # output_path=get_stylepro_artistic()   # ok
    output_path = get_stgan_bald()  # ok
    print(output_path)
    print("Done!")


def main6():
    res, output_path = get_pyramidbox_lite_server_mask()
    print(res)
    print(output_path)
    print("Done!")


def main7():
    output_path = get_deoldify()  # 'msg': "We only support 'to_tensor()' in dynamic graph mode, please call 'paddle.disable_static()' to enter dynamic graph mode."
    # output_path=get_user_guided_colorization()
    # output_path=get_photo_restoration()
    # output_path=get_animegan_v1_hayao_60()
    print(output_path)
    print("Done!")


def main8():
    res = get_humanseg_server()
    print(res)
    print("Done!")


if __name__ == '__main__':
    # main1()   # [{'国宝大熊猫': 0.9177336692810059}]
    # main2()     # bug:"We only support 'to_tensor()' in dynamic graph mode, please call 'paddle.disable_static()' to enter dynamic graph mode."
    # main3()     # chinese_ocr_db_crnn_server_result\ndarray_1615726863.3125894.jpg
    # main4()    # yolov3_resnet50_vd_coco2017_result\image_numpy_0.jpg
    # main5()    #  H:\leiproject\AI_Tools_v2\stgan_bald_result\2021-03-14-20-49-31.png  H:\leiproject\AI_Tools_v2\stylepro_artistic_result\2021-03-14-20-53-32.png
    # main6()     # .\pyramidbox_lite_server_mask_result\ndarray_time=1615726094558547.0.jpg
    main7()  #
    # main8()       # H:\leiproject\AI_Tools_v2\humanseg_server_result\2021-03-14-20-28-02.png
