
from bs4 import BeautifulSoup

html = '''
<ul class="list_mainnews">
			<li data-tiara-layer="MCC cluster2">
					<a href="https://news.v.daum.net/v/20211124112535532" class="link_thumb" data-tiara-layer="article_thumb" data-tiara-id="20211124112535532" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124112535532">
						<img src="https://img1.daumcdn.net/thumb/S112x90ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202111%2F24%2FZDNetKorea%2F20211124112537798lolx.jpg&scode=media" class="thumb_g" alt="알뜰폰 가입자 1천만 돌파..데이터 도매대가 30% 인하">
					</a>
				<div class="cont_thumb">
					<strong class="tit_thumb">
						<a href="https://news.v.daum.net/v/20211124112535532" class="link_txt" data-tiara-layer="article_main" data-tiara-id="20211124112535532" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124112535532">알뜰폰 가입자 1천만 돌파..데이터 도매대가 30% 인하</a>
					</strong>
					<span class="info_thumb">
                        지디넷코리아
                        <span class="txt_middot">·</span>
                        <span class="ico_news2 ico_cmt"><span class="screen_out">댓글수</span>17</span>
                    </span>
				</div>
				<div class="relate_news">
					<strong class="screen_out">연관 기사</strong>
							<div class="item_relate">
								<a href="https://news.v.daum.net/v/20211124103000025" class="link_txt" data-tiara-layer="article_sub" data-tiara-id="20211124103000025" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124103000025"">
	                                알뜰폰 1천만 시대, 요금제 더 싸진다..도매대가 인하
								</a>
								<span class="info_news">데일리안</span>
							</div>
				</div>
			</li>
			<li data-tiara-layer="MCC cluster3">
					<a href="https://news.v.daum.net/v/20211124141116948" class="link_thumb" data-tiara-layer="article_thumb" data-tiara-id="20211124141116948" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124141116948">
						<img src="https://img1.daumcdn.net/thumb/S112x90ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202111%2F24%2FNEWS1%2F20211124141116807ajjv.jpg&scode=media" class="thumb_g" alt="알뜰폰 1000만명 시대..통신자회사 점유율·추가 성장동력 고민도">
					</a>
				<div class="cont_thumb">
					<strong class="tit_thumb">
						<a href="https://news.v.daum.net/v/20211124141116948" class="link_txt" data-tiara-layer="article_main" data-tiara-id="20211124141116948" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124141116948">알뜰폰 1000만명 시대..통신자회사 점유율·추가 성장동력 고민도</a>
					</strong>
					<span class="info_thumb">
                        뉴스1
                        <span class="txt_middot">·</span>
                        <span class="ico_news2 ico_cmt"><span class="screen_out">댓글수</span>2</span>
                    </span>
				</div>
				<div class="relate_news">
					<strong class="screen_out">연관 기사</strong>
						<p class="desc_thumb">(서울=뉴스1) 김정현 기자 = 알뜰폰이 출범 11년만에 가입자 1000만명 시대를 맞았다. '가계통신요금 인하'라는 목표를 갖고 출범한 알뜰폰의 시장 정착이 성공했지만, 이동통신3사 자회사 점유율 문제, 추가 성장동력 문제 등 알뜰폰 시장을 둘러싼 과제는 여전히 산적한 상태다. ◇알뜰폰, 추가 성장 위해 e심·추가 도매대가 인하 등 마련 24일 과학</p>
				</div>
			</li>
			<li data-tiara-layer="MCC cluster4">
					<a href="https://news.v.daum.net/v/20211124162610539" class="link_thumb" data-tiara-layer="article_thumb" data-tiara-id="20211124162610539" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124162610539">
						<img src="https://img1.daumcdn.net/thumb/S112x90ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202111%2F24%2Fmoneytoday%2F20211124162611207rjjb.jpg&scode=media" class="thumb_g" alt="美 출장 마친 이재용 &quot;반도체 시장 냉혹한 현실에 마음 무거워&quot;">
					</a>
				<div class="cont_thumb">
					<strong class="tit_thumb">
						<a href="https://news.v.daum.net/v/20211124162610539" class="link_txt" data-tiara-layer="article_main" data-tiara-id="20211124162610539" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124162610539">美 출장 마친 이재용 "반도체 시장 냉혹한 현실에 마음 무거워"</a>
					</strong>
					<span class="info_thumb">
                        머니투데이
                        <span class="txt_middot">·</span>
                        <span class="ico_news2 ico_cmt"><span class="screen_out">댓글수</span>20</span>
                    </span>
				</div>
				<div class="relate_news">
					<strong class="screen_out">연관 기사</strong>
						<p class="desc_thumb">이재용 삼성전자 부회장이 테일러시 파운드리 신규 공장 신설 투자 발표와 관련 "투자도 투자지만 우리 현장의 투자자 목소리들, 시장의 냉혹한 현실을 직접 보고 오게 되니까 마음이 무겁다"고 말했다. 코로나19(COVID-19)이후 닥친 글로벌 반도체 공급난, 미중 반도체 패권 경쟁 등으로 인한 반도체 업황 위기를 엄중히 인식한 것이다. 미국 출장에서 귀국</p>
				</div>
			</li>
			<li data-tiara-layer="MCC cluster5">
					<a href="https://news.v.daum.net/v/20211124175705737" class="link_thumb" data-tiara-layer="article_thumb" data-tiara-id="20211124175705737" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124175705737">
						<img src="https://img1.daumcdn.net/thumb/S112x90ht.u/?fname=https%3A%2F%2Ft1.daumcdn.net%2Fnews%2F202111%2F24%2Fmk%2F20211124202710476jbsm.jpg&scode=media" class="thumb_g" alt="미국 20조원 투자 확정 짓고 귀국한 이재용의 첫마디">
					</a>
				<div class="cont_thumb">
					<strong class="tit_thumb">
						<a href="https://news.v.daum.net/v/20211124175705737" class="link_txt" data-tiara-layer="article_main" data-tiara-id="20211124175705737" data-tiara-type="harmony" data-tiara-ordnum="1" data-tiara-custom="contentUniqueKey=hamny-20211124175705737">미국 20조원 투자 확정 짓고 귀국한 이재용의 첫마디</a>
					</strong>
					<span class="info_thumb">
                        매일경제
                        <span class="txt_middot">·</span>
                        <span class="ico_news2 ico_cmt"><span class="screen_out">댓글수</span>19</span>
                    </span>
				</div>
				<div class="relate_news">
					<strong class="screen_out">연관 기사</strong>
						<p class="desc_thumb">◆ 삼성전자 美 20조 투자 ◆ "현장의 처절한 목소리와 시장의 냉혹한 현실을 직접 보고 오니 마음이 무겁다." 지난 14일 5년 만에 미국 출장을 떠난 이재용 삼성전자 부회장(사진)이 24일 김포공항을 통해 귀국했다. 공항에서 취재진과 만난 그는 출장과 관련해 네트워크 강화에 의미를 뒀다. 그는 "오랫동안 만나지 못했던 오래된 비즈니스 파트너들과 회포</p>
				</div>
			</li>
	</ul>
'''


soup = BeautifulSoup(html, 'html.parser')


print('=' * 40)
'''
# 기사 제목 추출 
title = soup.select_one('.cont_thumb > strong > a')
print(title.text)

# 신문사 이름 추출
newspaper_name = soup.select_one('.cont_thumb > .info_thumb')
txt = newspaper_name.text.strip()

txt = txt[0: txt.find('·')].strip()
print(txt)
'''

cont_list = soup.select('.cont_thumb')
# print(len(cont_list))
# print(cont_list)

for div in cont_list:
    # title = div.find('a', class_='link_txt').text
    title = div.select_one('strong > a.link_txt').text
    print(title)

    newspaper_name = div.select_one('.info_thumb')
    txt = newspaper_name.text.strip()
    txt = txt[0: txt.find('·')].strip()
    print(txt)

    print('=' * 40)