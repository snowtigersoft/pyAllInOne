#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Zhaochunyou <zhaochunyou@gmail.com>

import hashlib
import re
import time
import urllib
import urlparse

import requests

__author__ = 'zhaochunyou'


class PaymentMethod(object):
    """
    付款方式。
    """

    """
    不指定付款方式。
    """
    ALL = 'ALL'

    """
    信用卡付費。
    """
    Credit = 'Credit'

    """
    網路 ATM。
    """
    WebATM = 'WebATM'

    """
      自動櫃員機。
     """
    ATM = 'ATM'

    """
      超商代碼。
     """
    CVS = 'CVS'

    """
      超商條碼。
     """
    BARCODE = 'BARCODE'

    """
      支付寶。
     """
    Alipay = 'Alipay'

    """
      財付通。
     """
    Tenpay = 'Tenpay'

    """
      儲值消費。
     """
    TopUpUsed = 'TopUpUsed'


class PaymentMethodItem(object):
    """
    付款方式子項目。
    """

    """
      不指定。
     """
    Undefined = ''
    # WebATM 類(001~100)
    """
      台新銀行。
     """
    WebATM_TAISHIN = 'TAISHIN'

    """
      玉山銀行。
     """
    WebATM_ESUN = 'ESUN'

    """
      華南銀行。
     """
    WebATM_HUANAN = 'HUANAN'

    """
      台灣銀行。
     """
    WebATM_BOT = 'BOT'

    """
      台北富邦。
     """
    WebATM_FUBON = 'FUBON'

    """
      中國信託。
     """
    WebATM_CHINATRUST = 'CHINATRUST'

    """
      第一銀行。
     """
    WebATM_FIRST = 'FIRST'

    """
      國泰世華。
     """
    WebATM_CATHAY = 'CATHAY'

    """
      兆豐銀行。
     """
    WebATM_MEGA = 'MEGA'

    """
      元大銀行。
     """
    WebATM_YUANTA = 'YUANTA'

    """
      土地銀行。
     """
    WebATM_LAND = 'LAND'
    # ATM 類(101~200)
    """
      台新銀行。
     """
    ATM_TAISHIN = 'TAISHIN'

    """
      玉山銀行。
     """
    ATM_ESUN = 'ESUN'

    """
      華南銀行。
     """
    ATM_HUANAN = 'HUANAN'

    """
      台灣銀行。
     """
    ATM_BOT = 'BOT'

    """
      台北富邦。
     """
    ATM_FUBON = 'FUBON'

    """
      中國信託。
     """
    ATM_CHINATRUST = 'CHINATRUST'

    """
      第一銀行。
     """
    ATM_FIRST = 'FIRST'
    # 超商類(201~300)
    """
      超商代碼繳款。
     """
    CVS = 'CVS'

    """
      OK超商代碼繳款。
     """
    CVS_OK = 'OK'

    """
      全家超商代碼繳款。
     """
    CVS_FAMILY = 'FAMILY'

    """
      萊爾富超商代碼繳款。
     """
    CVS_HILIFE = 'HILIFE'

    """
      7-11 ibon代碼繳款。
     """
    CVS_IBON = 'IBON'
    # 其他第三方支付類(301~400)
    """
      支付寶。
     """
    Alipay = 'Alipay'

    """
      財付通。
     """
    Tenpay = 'Tenpay'
    # 儲值/餘額消費類(401~500)
    """
      儲值/餘額消費(歐付寶)
     """
    TopUpUsed_AllPay = 'AllPay'

    """
      儲值/餘額消費(玉山)
     """
    TopUpUsed_ESUN = 'ESUN'
    # 其他類(901~999)
    """
      超商條碼繳款。
     """
    BARCODE = 'BARCODE'

    """
      信用卡(MasterCard/JCB/VISA)。
     """
    Credit = 'Credit'

    """
      貨到付款。
     """
    COD = 'COD'


class ExtraPaymentInfo(object):
    """
  額外付款資訊。
 """

    """
      需要額外付款資訊。
     """
    Yes = 'Y'

    """
      不需要額外付款資訊。
     """
    No = 'N'


class DeviceType(object):
    """
  額外付款資訊。
 """
    """
      桌機版付費頁面。
     """
    PC = 'P'

    """
      行動裝置版付費頁面。
     """
    Mobile = 'M'


class ActionType(object):
    """
    信用卡訂單處理動作資訊。
    """

    """
      關帳
     """
    C = 'C'

    """
      退刷
     """
    R = 'R'

    """
      取消
     """
    E = 'E'

    """
      放棄
     """
    N = 'N'


class PeriodType(object):
    """
  定期定額的週期種類。
 """
    """
      無
     """
    Undefined = ''

    """
      年
     """
    Year = 'Y'

    """
      月
     """
    Month = 'M'

    """
      日
     """
    Day = 'D'


class InvoiceState(object):
    """
電子發票開立註記。
"""

    # 需要開立電子發票。
    Yes = 'Y'

    # 不需要開立電子發票。
    No = ''


class CarruerType(object):
    """
電子發票載具類別
"""
    # 無載具
    Undefined = ''

    # 會員載具
    Member = '1'

    # 買受人自然人憑證
    Citizen = '2'

    # 買受人手機條碼
    Cellphone = '3'


class PrintMark(object):
    """
  電子發票列印註記
 """

    # 不列印
    No = '0'

    # 列印
    Yes = '1'


class Donation(object):
    """
  電子發票捐贈註記
 """
    # 捐贈
    Yes = '1'

    # 不捐贈
    No = '2'


class ClearanceMark(object):
    """
  通關方式
 """
    # 經海關出口
    Yes = '1'

    # 非經海關出口
    No = '2'


class TaxType(object):
    """
  課稅類別
 """
    # 應稅
    Dutiable = '1'

    # 零稅率
    Zero = '2'

    # 免稅
    Free = '3'

    # 應稅與免稅混合(限收銀機發票無法分辦時使用，且需通過申請核可)
    Mix = '9'


class InvType(object):
    """
  字軌類別
 """
    # 一般稅額
    General = '07'

    # 特種稅額
    Special = '08'


class EncryptType(object):
    # hashlib.md5(預設).hexdigest()
    ENC_MD5 = 0

    # SHA256
    ENC_SHA256 = 1


def ksort(d):
    return [(k, d[k]) for k in sorted(d.keys())]


def uksort(d, keyfunc):
    return [(k, d[k]) for k in sorted(d.keys(), key=keyfunc)]


class AllInOne:
    """
      AllInOne short summary.

      AllInOne description.

      @version 1.0
      @author chunyou.zhao
    """
    ServiceURL = ''
    ServiceMethod = 'POST'
    HashKey = ''
    HashIV = ''
    MerchantID = ''
    Sandbox = False
    PaymentType = 'aio'
    Send = None
    SendExtend = None
    Query = None
    Action = None
    ChargeBack = None
    EncryptType = EncryptType.ENC_MD5

    def __init__(self, hash_key, hash_iv, merchant_id, sandbox=False):
        self.Sandbox = sandbox
        self.HashKey = hash_key
        self.HashIV = hash_iv
        self.MerchantID = merchant_id
        self.PaymentType = 'aio'
        self.Send = {
            "ReturnURL": '',
            "ClientBackURL": '',
            "OrderResultURL": '',
            "MerchantTradeNo": '',
            "MerchantTradeDate": '',
            "PaymentType": 'aio',
            "TotalAmount": '',
            "TradeDesc": '',
            "ChoosePayment": PaymentMethod.ALL,
            "Remark": '',
            "ChooseSubPayment": PaymentMethodItem.Undefined,
            "NeedExtraPaidInfo": ExtraPaymentInfo.No,
            "DeviceSource": DeviceType.PC,
            "IgnorePayment": '',
            "PlatformID": '',
            "InvoiceMark": InvoiceState.No,
            "Items": [],
            "EncryptType": EncryptType.ENC_MD5
        }
        self.SendExtend = {
            # ATM 延伸參數。
            "ExpireDate": 3,
            # CVS, BARCODE 延伸參數。
            "Desc_1": '', "Desc_2": '', "Desc_3": '', "Desc_4": '',
            # ATM, CVS, BARCODE 延伸參數。
            "ClientRedirectURL": '',
            # Alipay 延伸參數。
            "Email": '', "PhoneNo": '', "UserName": '',
            # Tenpay 延伸參數。
            "ExpireTime": '',
            # Credit 分期延伸參數。
            "CreditInstallment": 0, "InstallmentAmount": 0, "Redeem": False, "UnionPay": False,
            # Credit 定期定額延伸參數。
            "PeriodAmount": '', "PeriodType": '', "Frequency": '', "ExecTimes": '',
            # 回傳網址的延伸參數。
            "PaymentInfoURL": '', "PeriodReturnURL": '',
            # 電子發票延伸參數。
            "CustomerIdentifier": '',
            "CarruerType": CarruerType.Undefined,
            "CustomerID": '',
            "Donation": Donation.No,
            "Print": PrintMark.No,
            "CustomerName": '',
            "CustomerAddr": '',
            "CustomerPhone": '',
            "CustomerEmail": '',
            "ClearanceMark": '',
            "CarruerNum": '',
            "LoveCode": '',
            "InvoiceRemark": '',
            "DelayDay": 0
        }
        self.Query = {
            'MerchantTradeNo': '', 'TimeStamp': ''
        }
        self.Action = {
            'MerchantTradeNo': '', 'TradeNo': '', 'Action': ActionType.C, 'TotalAmount': 0
        }
        self.ChargeBack = {
            'MerchantTradeNo': '', 'TradeNo': '', 'ChargeBackTotalAmount': 0, 'Remark': ''
        }

    def get_check_value(self, parameters, enc_type):
        sz_check_mac_value = uksort(parameters, str.lower)
        sz_check_mac_value.insert(0, ("HashKey", self.HashKey))
        sz_check_mac_value.append(('HashIV', self.HashIV))

        sz_check_mac_value = urllib.quote(urllib.urlencode(sz_check_mac_value), '+%').lower()
        # 取代為與 dotNet 相符的字元
        mapping_dict = {'-': '%2d', '_': '%5f', '.': '%2e', '!': '%21', '*': '%2a', '(': '%28', ')': '%29', '%2f': '%252f', '%3a': '%253a'}
        for key, val in mapping_dict.iteritems():
            sz_check_mac_value = sz_check_mac_value.replace(val, key)

        # CheckMacValue 壓碼
        if enc_type == EncryptType.ENC_SHA256:
            sz_check_mac_value = hashlib.sha256(sz_check_mac_value).hexdigest()
        else:
            sz_check_mac_value = hashlib.md5(sz_check_mac_value).hexdigest()

        return sz_check_mac_value.upper()

    def check_out(self, target="_self"):
        return self.check_out_string(None, target)

    def check_out_string(self, payment_button, target="_self"):
        if self.Sandbox:
            self.ServiceURL = 'http://payment-stage.allpay.com.tw/Cashier/AioCheckOut'
        else:
            self.ServiceURL = 'https://payment.allpay.com.tw/Cashier/AioCheckOut'
        # 變數宣告。
        errors = []
        html = ''

        sz_item_name = ''
        sz_alipay_item_name = ''
        sz_alipay_item_counts = ''
        sz_alipay_item_price = ''
        sz_invoice_item_name = ''
        sz_invoice_item_count = ''
        sz_invoice_item_word = ''
        sz_invoice_item_price = ''
        sz_invoice_item_tax_type = ''
        inv_sper = '|'
        # 檢查資料。
        if len(self.ServiceURL) == 0:
            errors.append('ServiceURL is required.')

        if len(self.ServiceURL) > 200:
            errors.append('ServiceURL max length as 200.')

        if len(self.HashKey) == 0:
            errors.append('HashKey is required.')

        if len(self.HashIV) == 0:
            errors.append('HashIV is required.')

        if len(self.MerchantID) == 0:
            errors.append('MerchantID is required.')

        if len(self.MerchantID) > 10:
            errors.append('MerchantID max length as 10.')

        if 'ReturnURL' not in self.Send or len(self.Send['ReturnURL']) == 0:
            errors.append('ReturnURL is required.')

        if len(self.Send['ClientBackURL']) > 200:
            errors.append('ClientBackURL max length as 200.')

        if len(self.Send['OrderResultURL']) > 200:
            errors.append('OrderResultURL max length as 200.')

        if 'MerchantTradeNo' not in self.Send or len(self.Send['MerchantTradeNo']) == 0:
            errors.append('MerchantTradeNo is required.')

        if len(self.Send['MerchantTradeNo']) > 20:
            errors.append('MerchantTradeNo max length as 20.')

        if 'MerchantTradeDate' not in self.Send or len(self.Send['MerchantTradeDate']) == 0:
            errors.append('MerchantTradeDate is required.')

        if 'TotalAmount' not in self.Send:
            errors.append('TotalAmount is required.')

        if 'TradeDesc' not in self.Send:
            errors.append('TradeDesc is required.')

        if len(self.Send['TradeDesc']) > 200:
            errors.append('TradeDesc max length as 200.')

        if 'ChoosePayment' not in self.Send:
            errors.append('ChoosePayment is required.')

        if 'NeedExtraPaidInfo' not in self.Send:
            errors.append('NeedExtraPaidInfo is required.')

        if 'DeviceSource' not in self.Send:
            errors.append('DeviceSource is required.')

        if 'Items' not in self.Send:
            errors.append('Items is required.')

        # 檢查 Alipay 條件。
        if self.Send['ChoosePayment'] == PaymentMethod.Alipay:
            if len(self.SendExtend['Email']) == 0:
                errors.append("Email is required.")

            if len(self.SendExtend['Email']) > 200:
                errors.append("Email max length as 200.")

            if len(self.SendExtend['PhoneNo']) == 0:
                errors.append("PhoneNo is required.")

            if len(self.SendExtend['PhoneNo']) > 20:
                errors.append("PhoneNo max length as 20.")

            if len(self.SendExtend['UserName']) == 0:
                errors.append("UserName is required.")

            if len(self.SendExtend['UserName']) > 20:
                errors.append("UserName max length as 20.")

        # 檢查產品名稱。
        if len(self.Send['Items']) > 0:
            for item in self.Send['Items']:
                sz_item_name += u'#%s %d %s x %u' % (item['Name'], item['Price'], item['Currency'], item['Quantity'])
                sz_alipay_item_name += u'#%s' % item['Name']
                sz_alipay_item_counts += u'#%u' % item['Quantity']
                sz_alipay_item_price += u'#%d' % item['Price']

                if 'ItemURL' not in self.Send:
                    self.Send['ItemURL'] = item['URL']

            if len(sz_item_name) > 0:
                sz_item_name = sz_item_name[1:200]

            if len(sz_alipay_item_name) > 0:
                sz_alipay_item_name = sz_alipay_item_name[1:200]

            if len(sz_alipay_item_counts) > 0:
                sz_alipay_item_counts = sz_alipay_item_counts[1:100]

            if len(sz_alipay_item_price) > 0:
                sz_alipay_item_price = sz_alipay_item_price[1:20]

        else:
            errors.append("Goods information not found.")

        # 檢查電子發票參數
        if len(self.Send['InvoiceMark']) > 1:
            errors.append("InvoiceMark max length as 1.")
        else:
            if self.Send['InvoiceMark'] == InvoiceState.Yes:
                # RelateNumber(不可為空)
                if len(self.SendExtend['RelateNumber']) == 0:
                    errors.append("RelateNumber is required.")
                elif len(self.SendExtend['RelateNumber']) > 30:
                    errors.append("RelateNumber max length as 30.")

                # CustomerIdentifier(預設為空字串)
                if len(self.SendExtend['CustomerIdentifier']) > 0 and len(self.SendExtend['CustomerIdentifier']) != 8:
                    errors.append("CustomerIdentifier length should be 8.")

                # CarruerType(預設為None)
                if len(self.SendExtend['CarruerType']) > 1:
                    errors.append("CarruerType max length as 1.")
                else:
                    # 統一編號不為空字串時，載具類別請設定空字串
                    if len(self.SendExtend['CustomerIdentifier']) > 0 and \
                                    self.SendExtend['CarruerType'] != CarruerType.Undefined:
                        errors.append("CarruerType should be None.")

                # CustomerID(預設為空字串)
                if len(self.SendExtend['CustomerID']) > 20:
                    errors.append("CustomerID max length as 20.")
                else:
                    # 當載具類別為會員載具(Member)時，此參數不可為空字串
                    if self.SendExtend['CarruerType'] == CarruerType.Member and len(self.SendExtend['CustomerID']) == 0:
                        errors.append("CustomerID is required.")

                # Donation(預設為No)
                if len(self.SendExtend['Donation']) > 1:
                    errors.append("Donation max length as 1.")
                else:
                    # 統一編號不為空字串時，請設定不捐贈(No)
                    if len(self.SendExtend['CustomerIdentifier']) > 0:
                        if self.SendExtend['Donation'] != Donation.No:
                            errors.append("Donation should be No.")
                    elif len(self.SendExtend['Donation']) == 0:
                        self.SendExtend['Donation'] = Donation.No

                # Print(預設為No)
                if len(self.SendExtend['Print']) > 1:
                    errors.append("Print max length as 1.")
                else:
                    # 捐贈註記為捐贈(Yes)時，請設定不列印(No)
                    if self.SendExtend['Donation'] == Donation.Yes:
                        if self.SendExtend['Print'] != PrintMark.No:
                            errors.append("Print should be No.")
                    else:
                        # 統一編號不為空字串時，請設定列印(Yes)
                        if len(self.SendExtend['CustomerIdentifier']) > 0:
                            if self.SendExtend['Print'] != PrintMark.Yes:
                                errors.append("Print should be Yes.")

                        else:
                            if len(self.SendExtend['Print']) == 0:
                                self.SendExtend['Print'] = PrintMark.No

                            # 載具類別為會員載具(Member)、買受人自然人憑證(Citizen)、買受人手機條碼(Cellphone)時，請設定不列印(No)
                            not_print = [CarruerType.Member, CarruerType.Citizen, CarruerType.Cellphone]
                            if self.SendExtend['CarruerType'] in not_print \
                                    and self.SendExtend['Print'] == PrintMark.Yes:
                                errors.append("Print should be No.")

                # CustomerName(UrlEncode, 預設為空字串)
                if len(self.SendExtend['CustomerName']) > 20:
                    errors.append("CustomerName max length as 20.")
                else:
                    # 列印註記為列印(Yes)時，此參數不可為空字串
                    if self.SendExtend['Print'] == PrintMark.Yes:
                        if len(self.SendExtend['CustomerName']) == 0:
                            errors.append("CustomerName is required.")

                # CustomerAddr(UrlEncode, 預設為空字串)
                if len(self.SendExtend['CustomerAddr']) > 200:
                    errors.append("CustomerAddr max length as 200.")
                else:
                    # 列印註記為列印(Yes)時，此參數不可為空字串
                    if self.SendExtend['Print'] == PrintMark.Yes:
                        if len(self.SendExtend['CustomerAddr']) == 0:
                            errors.append("CustomerAddr is required.")

                # CustomerPhone(與CustomerEmail擇一不可為空)
                if len(self.SendExtend['CustomerPhone']) > 20:
                    errors.append("CustomerPhone max length as 20.")

                # CustomerEmail(UrlEncode, 預設為空字串, 與CustomerPhone擇一不可為空)
                if len(self.SendExtend['CustomerEmail']) > 200:
                    errors.append("CustomerEmail max length as 200.")

                if len(self.SendExtend['CustomerPhone']) == 0 and len(self.SendExtend['CustomerEmail']) == 0:
                    errors.append("CustomerPhone or CustomerEmail is required.")

                # TaxType(不可為空)
                if len(self.SendExtend['TaxType']) > 1:
                    errors.append("TaxType max length as 1.")
                else:
                    if len(self.SendExtend['TaxType']) == 0:
                        errors.append("TaxType is required.")

                # ClearanceMark(預設為空字串)
                if len(self.SendExtend['ClearanceMark']) > 1:
                    errors.append("ClearanceMark max length as 1.")
                else:
                    # 請設定空字串，僅課稅類別為零稅率(Zero)時，此參數不可為空字串
                    if self.SendExtend['TaxType'] == TaxType.Zero:
                        if self.SendExtend['ClearanceMark'] != ClearanceMark.Yes \
                                and self.SendExtend['ClearanceMark'] != ClearanceMark.No:
                            errors.append("ClearanceMark is required.")
                    else:
                        if len(self.SendExtend['ClearanceMark']) > 0:
                            errors.append("Please remove ClearanceMark.")

                # CarruerNum(預設為空字串)
                if len(self.SendExtend['CarruerNum']) > 64:
                    errors.append("CarruerNum max length as 64.")
                else:
                    # 載具類別為無載具(None)或會員載具(Member)時，請設定空字串
                    if self.SendExtend['CarruerType'] in [CarruerType.Undefined, CarruerType.Member]:
                        if len(self.SendExtend['CarruerNum']) > 0:
                            errors.append("Please remove CarruerNum.")
                    # 載具類別為買受人自然人憑證(Citizen)時，請設定自然人憑證號碼，前2碼為大小寫英文，後14碼為數字
                    elif self.SendExtend['CarruerType'] == CarruerType.Citizen:
                        if not re.search(r'/^[a-zA-Z]{2}\d{14}$/', self.SendExtend['CarruerNum']):
                            errors.append("Invalid CarruerNum.")
                    # 載具類別為買受人手機條碼(Cellphone)時，請設定手機條碼，第1碼為「/」，後7碼為大小寫英文、數字、「+」、「-」或「.」
                    elif self.SendExtend['CarruerType'] == CarruerType.Cellphone:
                        if not re.search(r'/^\/{1}[0-9a-zA-Z+-.]{7}$/', self.SendExtend['CarruerNum']):
                            errors.append("Invalid CarruerNum.")
                    else:
                        errors.append("Please remove CarruerNum.")

                # LoveCode(預設為空字串)
                # 捐贈註記為捐贈(Yes)時，參數長度固定3~7碼，請設定全數字或第1碼大小寫「X」，後2~6碼全數字
                if self.SendExtend['Donation'] == Donation.Yes:
                    if not re.search(r'/^([xX]{1}[0-9]{2,6}|[0-9]{3,7})$/', self.SendExtend['LoveCode']):
                        errors.append("Invalid LoveCode.")
                else:
                    if len(self.SendExtend['LoveCode']) > 0:
                        errors.append("Please remove LoveCode.")

                # InvoiceItemName(UrlEncode, 不可為空)
                # InvoiceItemCount(不可為空)
                # InvoiceItemWord(UrlEncode, 不可為空)
                # InvoiceItemPrice(不可為空)
                # InvoiceItemTaxType(不可為空)
                if len(self.SendExtend['InvoiceItems']) > 0:
                    tmp_item_name = []
                    tmp_item_count = []
                    tmp_item_word = []
                    tmp_item_price = []
                    tmp_item_tax_type = []
                    for tmpItemInfo in self.SendExtend['InvoiceItems']:
                        if len(tmpItemInfo['Name']) > 0:
                            tmp_item_name.append(tmpItemInfo['Name'])

                        if len(tmpItemInfo['Count']) > 0:
                            tmp_item_count.append(tmpItemInfo['Count'])

                        if len(tmpItemInfo['Word']) > 0:
                            tmp_item_word.append(tmpItemInfo['Word'])

                        if len(tmpItemInfo['Price']) > 0:
                            tmp_item_price.append(tmpItemInfo['Price'])

                        if len(tmpItemInfo['TaxType']) > 0:
                            tmp_item_tax_type.append(tmpItemInfo['TaxType'])

                    if self.SendExtend['TaxType'] == TaxType.Mix:
                        if TaxType.Dutiable in tmp_item_tax_type and TaxType.Free in tmp_item_tax_type:
                            # Do nothing
                            pass
                        else:
                            tmp_item_tax_type = []

                    if (len(tmp_item_name) + len(tmp_item_count) + len(tmp_item_word) + len(tmp_item_price) + len(
                            tmp_item_tax_type)) == (len(tmp_item_name) * 5):
                        sz_invoice_item_name = inv_sper.join(tmp_item_name)
                        sz_invoice_item_count = inv_sper.join(tmp_item_count)
                        sz_invoice_item_word = inv_sper.join(tmp_item_word)
                        sz_invoice_item_price = inv_sper.join(tmp_item_price)
                        sz_invoice_item_tax_type = inv_sper.join(tmp_item_tax_type)
                    else:
                        errors.append("Invalid Invoice Goods information.")

                else:
                    errors.append("Invoice Goods information not found.")

                # InvoiceRemark(UrlEncode, 預設為空字串)
                # DelayDay(不可為空, 預設為0)
                # 延遲天數，範圍0~15，設定為0時，付款完成後立即開立發票
                self.SendExtend['DelayDay'] = int(self.SendExtend['DelayDay'])
                if self.SendExtend['DelayDay'] < 0 or self.SendExtend['DelayDay'] > 15:
                    errors.append("DelayDay should be 0 ~ 15.")
                else:
                    if len(self.SendExtend['DelayDay']) == 0:
                        self.SendExtend['DelayDay'] = 0

                # InvType(不可為空)
                if len(self.SendExtend['InvType']) == 0:
                    errors.append("InvType is required.")

        # 檢查CheckMacValue加密方式
        if not isinstance(self.Send['EncryptType'], int):
            errors.append('EncryptType max length as 1.')

        # 輸出表單字串。
        if len(errors) == 0:
            # 信用卡特殊邏輯判斷(行動裝置畫面的信用卡分期處理，不支援定期定額)
            if self.Send['ChoosePayment'] == PaymentMethod.Credit \
                    and self.Send['DeviceSource'] == DeviceType.Mobile and not self.SendExtend['PeriodAmount']:
                self.Send['ChoosePayment'] = PaymentMethod.ALL
                self.Send['IgnorePayment'] = 'WebATM#ATM#CVS#BARCODE#Alipay#Tenpay#TopUpUsed#APPBARCODE#AccountLink'

            # 產生畫面控制項與傳遞參數。
            parameters = {
                'MerchantID': self.MerchantID,
                'PaymentType': self.PaymentType,
                'ItemName': sz_item_name,
                'ItemURL': self.Send['ItemURL'],
                'InvoiceItemName': sz_invoice_item_name,
                'InvoiceItemCount': sz_invoice_item_count,
                'InvoiceItemWord': sz_invoice_item_word,
                'InvoiceItemPrice': sz_invoice_item_price,
                'InvoiceItemTaxType': sz_invoice_item_tax_type
            }
            parameters.update(self.Send)
            parameters.update(self.SendExtend)
            # 處理延伸參數
            if not self.Send['PlatformID']:
                del parameters['PlatformID']
            # 整理全功能參數。
            if self.Send['ChoosePayment'] == PaymentMethod.ALL:
                del parameters['ExecTimes']
                del parameters['Frequency']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']

                parameters.update({
                    'AlipayItemName': sz_alipay_item_name,
                    'AlipayItemCounts': sz_alipay_item_counts,
                    'AlipayItemPrice': sz_alipay_item_price
                })

                if not parameters['CreditInstallment']:
                    del parameters['CreditInstallment']
                if not parameters['InstallmentAmount']:
                    del parameters['InstallmentAmount']
                if not parameters['Redeem']:
                    del parameters['Redeem']
                if not parameters['UnionPay']:
                    del parameters['UnionPay']

                if not self.Send['IgnorePayment']:
                    del parameters['IgnorePayment']
                if not self.SendExtend['ClientRedirectURL']:
                    del parameters['ClientRedirectURL']

            # 整理 Alipay 參數。
            if self.Send['ChoosePayment'] == PaymentMethod.Alipay:
                parameters.update({
                    'AlipayItemName': sz_alipay_item_name,
                    'AlipayItemCounts': sz_alipay_item_counts,
                    'AlipayItemPrice': sz_alipay_item_price
                })

                del parameters['CreditInstallment']
                del parameters['Desc_1']
                del parameters['Desc_2']
                del parameters['Desc_3']
                del parameters['Desc_4']
                del parameters['ExecTimes']
                del parameters['ExpireDate']
                del parameters['ExpireTime']
                del parameters['Frequency']
                del parameters['InstallmentAmount']
                del parameters['PaymentInfoURL']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']
                del parameters['Redeem']
                del parameters['UnionPay']

                del parameters['IgnorePayment']
                del parameters['ClientRedirectURL']

            # 整理 Tenpay 參數。
            if self.Send['ChoosePayment'] == PaymentMethod.Tenpay:
                del parameters['CreditInstallment']
                del parameters['Desc_1']
                del parameters['Desc_2']
                del parameters['Desc_3']
                del parameters['Desc_4']
                del parameters['Email']
                del parameters['ExecTimes']
                del parameters['ExpireDate']
                del parameters['Frequency']
                del parameters['InstallmentAmount']
                del parameters['PaymentInfoURL']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']
                del parameters['PhoneNo']
                del parameters['Redeem']
                del parameters['UnionPay']
                del parameters['UserName']

                del parameters['IgnorePayment']
                del parameters['ClientRedirectURL']

            # 整理 ATM 參數。
            if self.Send['ChoosePayment'] == PaymentMethod.ATM:
                del parameters['CreditInstallment']
                del parameters['Desc_1']
                del parameters['Desc_2']
                del parameters['Desc_3']
                del parameters['Desc_4']
                del parameters['Email']
                del parameters['ExecTimes']
                del parameters['ExpireTime']
                del parameters['Frequency']
                del parameters['InstallmentAmount']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']
                del parameters['PhoneNo']
                del parameters['Redeem']
                del parameters['UnionPay']
                del parameters['UserName']

                del parameters['IgnorePayment']
                if not self.SendExtend['ClientRedirectURL']:
                    del parameters['ClientRedirectURL']

            # 整理 BARCODE OR CVS 參數。
            if self.Send['ChoosePayment'] == PaymentMethod.BARCODE or self.Send['ChoosePayment'] == PaymentMethod.CVS:
                del parameters['CreditInstallment']
                del parameters['Email']
                del parameters['ExecTimes']
                del parameters['ExpireDate']
                del parameters['ExpireTime']
                del parameters['Frequency']
                del parameters['InstallmentAmount']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']
                del parameters['PhoneNo']
                del parameters['Redeem']
                del parameters['UnionPay']
                del parameters['UserName']

                del parameters['IgnorePayment']
                if not self.SendExtend['ClientRedirectURL']:
                    del parameters['ClientRedirectURL']

            # 整理全功能、WebATM OR TopUpUsed 參數。
            if self.Send['ChoosePayment'] in [PaymentMethod.WebATM, PaymentMethod.TopUpUsed]:
                del parameters['CreditInstallment']
                del parameters['Desc_1']
                del parameters['Desc_2']
                del parameters['Desc_3']
                del parameters['Desc_4']
                del parameters['Email']
                del parameters['ExecTimes']
                del parameters['ExpireDate']
                del parameters['ExpireTime']
                del parameters['Frequency']
                del parameters['InstallmentAmount']
                del parameters['PaymentInfoURL']
                del parameters['PeriodAmount']
                del parameters['PeriodReturnURL']
                del parameters['PeriodType']
                del parameters['PhoneNo']
                del parameters['Redeem']
                del parameters['UnionPay']
                del parameters['UserName']

                del parameters['IgnorePayment']
                del parameters['ClientRedirectURL']

            # 整理 Credit 參數。
            if self.Send['ChoosePayment'] == PaymentMethod.Credit:
                # Credit 分期。
                parameters['Redeem'] = 'Y' if parameters['Redeem'] else ''
                parameters['UnionPay'] = 1 if parameters['UnionPay'] else 0

                del parameters['Desc_1']
                del parameters['Desc_2']
                del parameters['Desc_3']
                del parameters['Desc_4']
                del parameters['Email']
                del parameters['ExpireDate']
                del parameters['ExpireTime']
                del parameters['PaymentInfoURL']
                del parameters['PhoneNo']
                del parameters['UserName']

                del parameters['IgnorePayment']
                del parameters['ClientRedirectURL']

            del parameters['Items']

            # 處理電子發票參數
            if 'InvoiceItems' in parameters:
                del parameters['InvoiceItems']
            if self.Send['InvoiceMark'] == InvoiceState.Yes:
                encode_fields = [
                    'CustomerName',
                    'CustomerAddr',
                    'CustomerEmail',
                    'InvoiceItemName',
                    'InvoiceItemWord',
                    'InvoiceRemark'
                ]
                for tmp_field in encode_fields:
                    parameters[tmp_field] = urllib.urlencode(parameters[tmp_field])
            else:
                if 'InvoiceMark' in parameters:
                    del parameters['InvoiceMark']
                if 'RelateNumber' in parameters:
                    del parameters['RelateNumber']
                if 'CustomerIdentifier' in parameters:
                    del parameters['CustomerIdentifier']
                if 'CarruerType' in parameters:
                    del parameters['CarruerType']
                if 'CustomerID' in parameters:
                    del parameters['CustomerID']
                if 'Donation' in parameters:
                    del parameters['Donation']
                if 'Print' in parameters:
                    del parameters['Print']
                if 'CustomerName' in parameters:
                    del parameters['CustomerName']
                if 'CustomerAddr' in parameters:
                    del parameters['CustomerAddr']
                if 'CustomerPhone' in parameters:
                    del parameters['CustomerPhone']
                if 'CustomerEmail' in parameters:
                    del parameters['CustomerEmail']
                if 'TaxType' in parameters:
                    del parameters['TaxType']
                if 'ClearanceMark' in parameters:
                    del parameters['ClearanceMark']
                if 'CarruerNum' in parameters:
                    del parameters['CarruerNum']
                if 'LoveCode' in parameters:
                    del parameters['LoveCode']
                if 'InvoiceItemName' in parameters:
                    del parameters['InvoiceItemName']
                if 'InvoiceItemCount' in parameters:
                    del parameters['InvoiceItemCount']
                if 'InvoiceItemWord' in parameters:
                    del parameters['InvoiceItemWord']
                if 'InvoiceItemPrice' in parameters:
                    del parameters['InvoiceItemPrice']
                if 'InvoiceItemTaxType' in parameters:
                    del parameters['InvoiceItemTaxType']
                if 'InvoiceRemark' in parameters:
                    del parameters['InvoiceRemark']
                if 'DelayDay' in parameters:
                    del parameters['DelayDay']
                if 'InvType' in parameters:
                    del parameters['InvType']

            sz_check_mac_value = self.get_check_value(parameters, self.Send['EncryptType'])

            html = '<meta http-equiv="Content-Type" content="text/html charset=utf-8" />'
            html += '<div style="text-align:center" ><form id="__allpayForm" method="post" target="' + \
                    target + '" action="' + self.ServiceURL + '">'
            for keys, value in parameters.iteritems():
                html += "<input type='hidden' name='%s' value='%s' />" % (keys, value)

            html += '<input type="hidden" name="CheckMacValue" value="' + sz_check_mac_value + '" />'
            # 手動或自動送出表單。
            if not payment_button:
                html += '<script type="text/javascript">document.getElementById("__allpayForm").submit()</script>'
            else:
                html += '<input type="submit" id="__paymentButton" value="' + payment_button + '" />'

            html += '</form></div>'

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return html

    def check_out_feedback(self, data):
        """
        :param data: POST data
        :return:
        """
        # 變數宣告。
        errors = []
        parameters = {}
        feedback = {}
        check_mac_value = ''
        # 重新整理回傳參數。
        for keys, value in data.iteritems():
            if keys != 'CheckMacValue':
                if keys == 'PaymentType':
                    value = value.replace('_CVS', '')
                    value = value.replace('_BARCODE', '')
                    value = value.replace('_Alipay', '')
                    value = value.replace('_Tenpay', '')
                    value = value.replace('_CreditCard', '')

                if keys == 'PeriodType':
                    value = value.replace('Y', 'Year')
                    value = value.replace('M', 'Month')
                    value = value.replace('D', 'Day')

                feedback[keys] = value
            else:
                check_mac_value = value

        # 回傳參數鍵值轉小寫。
        for keys, value in data.iteritems():
            if keys == 'view' or keys == 'hikashop_front_end_main':
                # Customize to Skip Parameters for HikaShop
                pass
            elif keys == 'mijoshop_store_id' or keys == 'language':
                # Customize to Skip Parameters for MijoShop
                pass
            else:
                parameters[keys.lower()] = value

        del parameters['checkmacvalue']

        # 驗證檢查碼。
        if len(feedback) > 0:
            confirm_mac_value = self.get_check_value(parameters, self.EncryptType)

            if check_mac_value != confirm_mac_value.upper():
                errors.append('CheckMacValue verify fail.')

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return feedback

    def query_trade_info(self):
        if self.Sandbox:
            self.ServiceURL = 'http://payment-stage.allpay.com.tw/Cashier/QueryTradeInfo'
        else:
            self.ServiceURL = 'https://payment.allpay.com.tw/Cashier/QueryTradeInfo'
        # 變數宣告。
        errors = []
        self.Query['TimeStamp'] = time.time()
        feedback = []
        confirm_args = {}
        # 檢查資料。
        if len(self.ServiceURL) == 0:
            errors.append('ServiceURL is required.')

        if len(self.ServiceURL) > 200:
            errors.append('ServiceURL max length as 200.')

        if len(self.HashKey) == 0:
            errors.append('HashKey is required.')

        if len(self.HashIV) == 0:
            errors.append('HashIV is required.')

        if len(self.MerchantID) == 0:
            errors.append('MerchantID is required.')

        if len(self.MerchantID) > 10:
            errors.append('MerchantID max length as 10.')

        if len(self.Query['MerchantTradeNo']) == 0:
            errors.append('MerchantTradeNo is required.')

        if len(self.Query['MerchantTradeNo']) > 20:
            errors.append('MerchantTradeNo max length as 20.')

        if len(self.Query['TimeStamp']) == 0:
            errors.append('TimeStamp is required.')

        # 呼叫查詢。
        if len(errors) == 0:
            parameters = {"MerchantID": self.MerchantID}
            parameters.update(self.Query)

            check_mac_value = self.get_check_value(parameters, EncryptType.ENC_MD5)

            parameters["CheckMacValue"] = check_mac_value
            # 送出查詢並取回結果。
            result = self.server_post(parameters)
            result = result.replace(' ', '%20')
            result = result.replace('+', '%2B')
            # 轉結果為陣列。
            parameters = urlparse.parse_qs(result)
            # 重新整理回傳參數。
            for keys, value in parameters.iteritems():
                if keys == 'CheckMacValue':
                    check_mac_value = value
                else:
                    feedback[keys] = value
                    confirm_args[keys.lower()] = value

            # 驗證檢查碼。
            if len(feedback) > 0:
                confirm_mac_value = self.get_check_value(confirm_args, EncryptType.ENC_MD5)

                if check_mac_value != confirm_mac_value.upper():
                    errors.append('CheckMacValue verify fail.')

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return feedback

    def query_period_credit_card_trade_info(self):
        if self.Sandbox:
            self.ServiceURL = 'http://payment-stage.allpay.com.tw/Cashier/QueryCreditCardTradeInfo'
        else:
            self.ServiceURL = 'https://payment.allpay.com.tw/Cashier/QueryCreditCardTradeInfo'
        # 變數宣告。
        errors = []
        self.Query['TimeStamp'] = time.time()
        feedback = []
        # 檢查資料。
        if len(self.ServiceURL) == 0:
            errors.append('ServiceURL is required.')

        if len(self.ServiceURL) > 200:
            errors.append('ServiceURL max length as 200.')

        if len(self.HashKey) == 0:
            errors.append('HashKey is required.')

        if len(self.HashIV) == 0:
            errors.append('HashIV is required.')

        if len(self.MerchantID) == 0:
            errors.append('MerchantID is required.')

        if len(self.MerchantID) > 10:
            errors.append('MerchantID max length as 10.')

        if len(self.Query['MerchantTradeNo']) == 0:
            errors.append('MerchantTradeNo is required.')

        if len(self.Query['MerchantTradeNo']) > 20:
            errors.append('MerchantTradeNo max length as 20.')

        if len(self.Query['TimeStamp']) == 0:
            errors.append('TimeStamp is required.')

        # 呼叫查詢。
        if len(errors) == 0:
            parameters = {"MerchantID": self.MerchantID}
            parameters.update(self.Query)

            parameters["CheckMacValue"] = self.get_check_value(parameters, EncryptType.ENC_MD5)
            # 送出查詢並取回結果。
            result = self.server_post(parameters)
            result = result.replace(' ', '%20')
            result = result.replace('+', '%2B')
            # 轉結果為陣列。
            feedback = urlparse.parse_qs(result)

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return feedback

    def do_action(self):
        if self.Sandbox:
            self.ServiceURL = 'http://payment-stage.allpay.com.tw/CreditDetail/DoAction'
        else:
            self.ServiceURL = 'https://payment.allpay.com.tw/CreditDetail/DoAction'
        # 變數宣告。
        errors = []
        feedback = {}
        # 檢查資料。
        if len(self.ServiceURL) == 0:
            errors.append('ServiceURL is required.')

        if len(self.ServiceURL) > 200:
            errors.append('ServiceURL max length as 200.')

        if len(self.HashKey) == 0:
            errors.append('HashKey is required.')

        if len(self.HashIV) == 0:
            errors.append('HashIV is required.')

        if len(self.MerchantID) == 0:
            errors.append('MerchantID is required.')

        if len(self.MerchantID) > 10:
            errors.append('MerchantID max length as 10.')

        if 'MerchantTradeNo' not in self.Action or len(self.Action['MerchantTradeNo']) == 0:
            errors.append('MerchantTradeNo is required.')

        if len(self.Action['MerchantTradeNo']) > 20:
            errors.append('MerchantTradeNo max length as 20.')

        if 'TradeNo' not in self.Action or len(self.Action['TradeNo']) == 0:
            errors.append('TradeNo is required.')

        if len(self.Action['TradeNo']) > 20:
            errors.append('TradeNo max length as 20.')

        if 'Action' not in self.Action or len(self.Action['Action']) == 0:
            errors.append('Action is required.')

        if len(self.Action['Action']) > 1:
            errors.append('Action max length as 1.')

        if self.Action.get('TotalAmount', 0) == 0:
            errors.append('TotalAmount is required.')

        # 呼叫信用卡訂單處理。
        if len(errors) == 0:
            parameters = {"MerchantID": self.MerchantID}
            parameters.update(self.Action)
            parameters["CheckMacValue"] = self.get_check_value(parameters, EncryptType.ENC_MD5)
            # 送出查詢並取回結果。
            result = self.server_post(parameters)
            # 轉結果為陣列。
            parameters = urlparse.parse_qs(result)
            # 重新整理回傳參數。
            for keys, value in parameters.iteritems():
                if keys == 'CheckMacValue':
                    sz_check_mac_value = value
                else:
                    feedback[keys] = value

            if 'RtnCode' in feedback and feedback['RtnCode'] != '1':
                errors.append(u'#%s: %s' % tuple([feedback['RtnCode'], feedback['RtnMsg']]))

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return feedback

    def aio_charge_back(self):
        if self.Sandbox:
            self.ServiceURL = 'http://payment-stage.allpay.com.tw/Cashier/AioChargeback'
        else:
            self.ServiceURL = 'https://payment.allpay.com.tw/Cashier/AioChargeback'
        # 變數宣告。
        errors = []
        parameters = {"MerchantID": self.MerchantID}
        parameters.update(self.ChargeBack)
        feedback = {}
        # 檢查資料。
        if len(self.ServiceURL) == 0:
            errors.append('ServiceURL is required.')

        if len(self.ServiceURL) > 200:
            errors.append('ServiceURL max length as 200.')

        if len(self.HashKey) == 0:
            errors.append('HashKey is required.')

        if len(self.HashIV) == 0:
            errors.append('HashIV is required.')

        if len(self.MerchantID) == 0:
            errors.append('MerchantID is required.')

        if len(self.MerchantID) > 10:
            errors.append('MerchantID max length as 10.')

        if len(self.ChargeBack['MerchantTradeNo']) == 0:
            errors.append('MerchantTradeNo is required.')

        if len(self.ChargeBack['MerchantTradeNo']) > 20:
            errors.append('MerchantTradeNo max length as 20.')

        if len(self.ChargeBack['TradeNo']) == 0:
            errors.append('TradeNo is required.')

        if len(self.ChargeBack['TradeNo']) > 20:
            errors.append('TradeNo max length as 20.')

        if self.ChargeBack['ChargeBackTotalAmount'] == 0:
            errors.append('ChargeBackTotalAmount is required.')

        if len(self.ChargeBack['Remark']) > 200:
            errors.append('Remark max length as 200.')

        parameters["CheckMacValue"] = self.get_check_value(parameters, EncryptType.ENC_MD5)
        # 送出查詢並取回結果。
        result = self.server_post(parameters)
        # 檢查結果資料。
        if result == '1|OK':
            feedback['RtnCode'] = '1'
            feedback['RtnMsg'] = 'OK'
        else:
            errors.append(result).replace('-', ': ')

        if len(errors) > 0:
            raise Exception('- '.join(errors))

        return feedback

    def server_post(self, parameters):
        res = requests.request(
                method=self.ServiceMethod,
                url=self.ServiceURL,
                params=parameters
        )
        return res.text
