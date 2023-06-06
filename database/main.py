# from contents import *
# from setting import session
# import csv

# def insert_faq(question, answer):
#     faq = Content(question=question, answer=answer)

# 	# 新規オブジェクトをsessionにadd()すると，INSERT対象になる．
#     session.add(faq)
#     session.commit()
#     session.refresh(faq)  # idを取得

#     return faq.id

# #MySQLにfaqデータを保存する処理
# def save_faq():
#     # CSVファイルからデータを読み込んでデータベースに保存する
#     csv_file_path = '/Users/hiraemizuhajime2/workspace/openai/customer/apps/web-crawl-q-and-a/processed/scraped.csv'
#     with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             question = row['text'].split('質問:')[1].split('回答:')[0].strip()
#             answer = row['text'].split('回答:')[1].strip()
            
#             # データベースに保存するオブジェクトを作成
#             qa = Content(question=question, answer=answer)
            
#             # オブジェクトをセッションに追加
#             session.add(qa)
        
#         # セッションをコミットしてデータベースに変更を保存
#         session.commit()

#     # セッションを閉じる
#     session.close()

# if __name__ == "__main__":
#     save_faq()