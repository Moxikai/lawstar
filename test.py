#coding:utf-8
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
str1 = """<div id="bg">
			<div id="xlpx2_left">
				<div class="ztfg_left1">
					<img src="/model/images/fgzw_dysc.jpg" width="176" height="32">
				</div>
				<div class="xlpx2_left2">
					<img src="/model/images/button1.jpg" width="115" height="27" onclick="javascript:PrintMe()" style="cursor: hand;">
					<!-- <a href="/pao?fn=chl345s142.txt&action=typeset"><img src="/model/images/button2.jpg"/></a>

					<img src="/model/images/button4.jpg" width="115" height="27" onclick="javascript:zl()" style="cursor: hand;"/>
					<div class="xlpx2_left1">
						正文转入：
						<br />
						<label>
							<select name="select" id="dic">
          					 	<option value="psl">请选择</option>
						    			<option value="2">常用法规</option>
							</select>
						</label>
					</div>
					-->
				</div>
				<div class="ztfg_left1">
					<img src="/model/images/fgzw_ftyy2.jpg" width="176" height="32">
				</div>
				<div class="fgzw_ftyy2">
					<ul>

						<li>
							<a target="_blank" href="/law?fn=chl173s112.txt">互联网信息服务管理办法</a>
						</li>
					</ul>
				</div>
				<div class="ztfg_left1">
					<img src="/model/images/fgzw_xgfg.jpg" width="176" height="32">
				</div>
				<div class="fgzw_ftyy2">
					<ul>
						<li>
							<a target="_blank" href="/law?fn=chl351s849.txt">国务院办公厅关于印发全国打击传销专项行动方案的通知</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=chl358s415.txt">国务院办公厅对《禁止传销条例》中传销查处认定部门解释的函</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=chl359s601.txt">国家工商行政管理总局、公安部关于在全国开展打击传销集中行动的通知</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=chl360s110.txt">国家工商行政管理总局关于出租房屋给传销人员居住的行为是否依据《禁止传销条例》进行处罚问...</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=chl378s680.txt">国家工商总局直销监督管理局、公安部经济犯罪侦查局关于做好“禁传销，保亚运”工作的通知</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=lar444s829.txt">东莞市人民政府办公室关于印发东莞市2005年打击传销和变相传销行动方案的通知</a>
						</li>
						<li>
							<a target="_blank" href="/law?fn=lar444s888.txt">广东省人民政府办公厅关于进一步加强打击传销和变相传销工作的通知</a>
						</li>
					</ul>
				</div>
				<!--
				<div class="ztfg_left1">
					<a href="#"><img src="/model/images/fgzw_xglw.jpg" width="176"
							height="32" />
					</a>
				</div>
				<div class="fgzw_ftyy2">
					<ul>
						<li>
							<a href="#">中央补助地方公共卫生专项资金农村卫生人员培训项目管理办法</a>
						</li>
						<li>
							<a href="#">国家税务总局关于下发20090601d版出口商品退税率文库的通知</a>
						</li>
						<li>
							<a href="#">中央补助地方公共卫生专项资金农村卫生人员培训项目管理办法</a>
						</li>
					</ul>
				</div>
				 -->
			</div>			<div id="globalAd" style="display:none" align="center">
			<img src="model/images/alert.gif" width="auto" height="auto" border="0" usemap="#Map">
			<map name="Map" id="Map">
				<area shape="rect" coords="264,1,300,31" onclick="closeGlobalAd();">
				<area shape="rect" coords="90,310,216,349" onclick="redirectUrlToActive();">
			</map>
		</div>
			<div id="fgzw_right" style="position: relative;">
				<div class="xlpx2_right0">
					<div class="xlpx2_right1" id="floattool">
						<script type="text/javascript">
				$("#dic").click(function(){
					 	$.ajax({
							type: "get",
							url: "/userlogin",
							data: "dbname=cook",
							success: function(data, textStatus){
						if(data==null||data==""){
			  			$("#dic").find("option").remove();
			  			var p = $(".fgzw_right2");
						var position = p.position();
						var left = position.left;
						var top = position.top;
			  		 $.ajax({
						type: "get",
						url: "/userdir",
						data: "action=ishow&ts=switch&tab=detail",
						success: function(data, textStatus){
							$("#wjj5").html(data);
							$("#wjj5").css({position: "absolute",top:top/2+3,left:-55});
						},
						complete: function(XMLHttpRequest, textStatus){
						//HideLoading();
						},
						error: function(){
						//请求出错处理
							}
						});
			  		  }}})
				});
				function zhuce(){
					$.ajax({
					type: "get",
					url: "/userdir",
					data: "action=ishow&ts=zhuce",
					success: function(data, textStatus){
						//alert(data);
						$("#wjj5").html(data);
					},
					complete: function(XMLHttpRequest, textStatus){
						//HideLoading();
					},
					error: function(){
						//请求出错处理
					}
				  });
				}
  		function elect(uu){
  			$("#wjj5").hide();
  			 location.reload();
  		}
			</script>
						<div id="wjj5" align="center"></div>
						<table width="100%" border="0" cellpadding="0" cellspacing="0">
							<tbody><tr>
								<td width="22" height="24" valign="middle">
									<span class="fdj">按</span>
								</td>
								<td width="120" valign="middle">
									<select id="showinfo" name="select5" onchange="javascript:donchang();">
										<option value="yes">
											索引信息+正文
										</option>
										<option value="no">
											正文
										</option>
									</select>
								</td>
								<td valign="middle">
									<span class="fdj">显示</span>
								</td>
								<td width="130" align="right" valign="middle">
									<span class="fdj" id="fdj">本篇关键字搜索：</span>
								</td>
								<td width="200" valign="middle">
									<input name="textfield" type="text" id="kw" size="40">
								</td>
								<td valign="middle">
									<img src="/model/images/chaxun2.jpg" width="53" height="21" onclick="javascript:FindItIE();" style="cursor: pointer;">
								</td>
							</tr>
						</tbody></table>
					</div>
				</div>
				<div class="fgzw_right2" id="fgzw_right2">
					<ul>
						<li id="tit">
							【法规标题】禁止传销条例
						</li>
						<li>
							【法规文号】444
						</li>
						<li id="tdat">
							【发布日期】20050823
						</li>
						<li>
							【实施日期】20051101
						</li>
						<li id="tdpt">
							【发布部门】国务院
						</li>
						<li>
							【效力等级】行政法规
						</li>
						 					</ul>
				</div>
				<div style="display: none">
					<form action="/linkserv" method="post" id="links" target="_blank">
						<input id="txr" name="rids">
					</form>
				</div>
				<p>
					<span class="fgzw_zw">【正文】</span>
					<!--
					<span class="fy">

						<img style="cursor:pointer;" src="/model/images/fy.gif" onclick="javascript:sub();" width="64" height="20" />
					</span>
					 -->
				</p>
				<div class="zhengwen" id="maintext">
					 <br><div align="center"><strong>禁止传销条例</strong></div>
<br><br><div align="center"><strong>中华人民共和国国务院令第４４４号</strong></div>
<br>   《禁止传销条例》已经２００５年８月１０日国务院第１０１次常务会议通过，现予公布，自２００５年１１月１日起施行。
<br>
<br><div align="right">总理温家宝</div><div align="right">二○○五年八月二十三日</div>
<br><br><div align="center"><strong>禁止传销条例</strong></div>
<br><br><div align="center"><strong>第一章  总则</strong></div>
<br>　　<b>第一条 </b> 为了防止欺诈，保护公民、法人和其他组织的合法权益，维护社会主义市场经济秩序，保持社会稳定，制定本条例。
<br>　　<b>第二条 </b> 本条例所称传销，是指组织者或者经营者发展人员，通过对被发展人员以其直接或者间接发展的人员数量或者销售业绩为依据计算和给付报酬，或者要求被发展人员以交纳一定费用为条件取得加入资格等方式牟取非法利益，扰乱经济秩序，影响社会稳定的行为。
<br>　　<b>第三条 </b> 县级以上地方人民政府应当加强对查处传销工作的领导，支持、督促各有关部门依法履行监督管理职责。
<br>　　县级以上地方人民政府应当根据需要，建立查处传销工作的协调机制，对查处传销工作中的重大问题及时予以协调、解决。
<br>　　<b>第四条 </b> 工商行政管理部门、公安机关应当依照本条例的规定，在各自的职责范围内查处传销行为。
<br>　　<b>第五条 </b> 工商行政管理部门、公安机关依法查处传销行为，应当坚持教育与处罚相结合的原则，教育公民、法人或者其他组织自觉守法。
<br>　　<b>第六条 </b> 任何单位和个人有权向工商行政管理部门、公安机关举报传销行为。工商行政管理部门、公安机关接到举报后，应当立即调查核实，依法查处，并为举报人保密；经调查属实的，依照国家有关规定对举报人给予奖励。
<br>
<br><br><div align="center"><strong>第二章  传销行为的种类与查处机关</strong></div>
<br>　　<b>第七条 </b> 下列行为，属于传销行为：
<br>　　（一）组织者或者经营者通过发展人员，要求被发展人员发展其他人员加入，对发展的人员以其直接或者间接滚动发展的人员数量为依据计算和给付报酬（包括物质奖励和其他经济利益，下同），牟取非法利益的；
<br>　　（二）组织者或者经营者通过发展人员，要求被发展人员交纳费用或者以认购商品等方式变相交纳费用，取得加入或者发展其他人员加入的资格，牟取非法利益的；
<br>　　（三）组织者或者经营者通过发展人员，要求被发展人员发展其他人员加入，形成上下线关系，并以下线的销售业绩为依据计算和给付上线报酬，牟取非法利益的。
<br>　　<b>第八条 </b> 工商行政管理部门依照本条例的规定，负责查处本条例第七条规定的传销行为。
<br>　　<b>第九条 </b> 利用互联网等媒体发布含有本条例第七条规定的传销信息的，由工商行政管理部门会同电信等有关部门依照本条例的规定查处。
<br>　　<b>第十条 </b> 在传销中以介绍工作、从事经营活动等名义欺骗他人离开居所地非法聚集并限制其人身自由的，由公安机关会同工商行政管理部门依法查处。
<br>　　<b>第十一条 </b> 商务、教育、民政、财政、劳动保障、电信、税务等有关部门和单位，应当依照各自职责和有关法律、行政法规的规定配合工商行政管理部门、公安机关查处传销行为。
<br>　　<b>第十二条 </b> 农村村民委员会、城市居民委员会等基层组织，应当在当地人民政府指导下，协助有关部门查处传销行为。
<br>　　<b>第十三条 </b> 工商行政管理部门查处传销行为，对涉嫌犯罪的，应当依法移送公安机关立案侦查；公安机关立案侦查传销案件，对经侦查不构成犯罪的，应当依法移交工商行政管理部门查处。
<br>
<br><br><div align="center"><strong>第三章  查处措施和程序</strong></div>
<br>　　<b>第十四条 </b> 县级以上工商行政管理部门对涉嫌传销行为进行查处时，可以采取下列措施：
<br>　　（一）责令停止相关活动；
<br>　　（二）向涉嫌传销的组织者、经营者和个人调查、了解有关情况；
<br>　　（三）进入涉嫌传销的经营场所和培训、集会等活动场所，实施现场检查；
<br>　　（四）查阅、复制、查封、扣押涉嫌传销的有关合同、票据、账簿等资料；
<br>　　（五）查封、扣押涉嫌专门用于传销的产品（商品）、工具、设备、原材料等财物；
<br>　　（六）查封涉嫌传销的经营场所；
<br>　　（七）查询涉嫌传销的组织者或者经营者的账户及与存款有关的会计凭证、账簿、对账单等；
<br>　　（八）对有证据证明转移或者隐匿违法资金的，可以申请司法机关予以冻结。
<br>　　工商行政管理部门采取前款规定的措施，应当向县级以上工商行政管理部门主要负责人书面或者口头报告并经批准。遇有紧急情况需要当场采取前款规定措施的，应当在事后立即报告并补办相关手续；其中，实施前款规定的查封、扣押，以及第（七）项、第（八）项规定的措施，应当事先经县级以上工商行政管理部门主要负责人书面批准。
<br>　　<b>第十五条 </b> 工商行政管理部门对涉嫌传销行为进行查处时，执法人员不得少于２人。
<br>　　执法人员与当事人有直接利害关系的，应当回避。
<br>　　<b>第十六条 </b> 工商行政管理部门的执法人员对涉嫌传销行为进行查处时，应当向当事人或者有关人员出示证件。
<br>　　<b>第十七条 </b> 工商行政管理部门实施查封、扣押，应当向当事人当场交付查封、扣押决定书和查封、扣押财物及资料清单。
<br>　　在交通不便地区或者不及时实施查封、扣押可能影响案件查处的，可以先行实施查封、扣押，并应当在24小时内补办查封、扣押决定书，送达当事人。
<br>　　<b>第十八条 </b> 工商行政管理部门实施查封、扣押的期限不得超过30日；案件情况复杂的，经县级以上工商行政管理部门主要负责人批准，可以延长15日。
<br>　　对被查封、扣押的财物，工商行政管理部门应当妥善保管，不得使用或者损毁；造成损失的，应当承担赔偿责任。但是，因不可抗力造成的损失除外。
<br>　　<b>第十九条 </b> 工商行政管理部门实施查封、扣押，应当及时查清事实，在查封、扣押期间作出处理决定。
<br>　　对于经调查核实属于传销行为的，应当依法没收被查封、扣押的非法财物；对于经调查核实没有传销行为或者不再需要查封、扣押的，应当在作出处理决定后立即解除查封，退还被扣押的财物。
<br>　　工商行政管理部门逾期未作出处理决定的，被查封的物品视为解除查封，被扣押的财物应当予以退还。拒不退还的，当事人可以向人民法院提起行政诉讼。
<br>　　<b>第二十条 </b> 工商行政管理部门及其工作人员违反本条例的规定使用或者损毁被查封、扣押的财物，造成当事人经济损失的，应当承担赔偿责任。
<br>　　<b>第二十一条 </b> 工商行政管理部门对涉嫌传销行为进行查处时，当事人有权陈述和申辩。
<br>　　<b>第二十二条 </b> 工商行政管理部门对涉嫌传销行为进行查处时，应当制作现场笔录。
<br>　　现场笔录和查封、扣押清单由当事人、见证人和执法人员签名或者盖章，当事人不在现场或者当事人、见证人拒绝签名或者盖章的，执法人员应当在现场笔录中予以注明。
<br>　　<b>第二十三条 </b> 对于经查证属于传销行为的，工商行政管理部门、公安机关可以向社会公开发布警示、提示。
<br>　　向社会公开发布警示、提示应当经县级以上工商行政管理部门主要负责人或者公安机关主要负责人批准。
<br>
<br><br><div align="center"><strong>第四章  法律责任</strong></div>
<br>　　<b>第二十四条 </b> 有本条例第七条规定的行为，组织策划传销的，由工商行政管理部门没收非法财物，没收违法所得，处50万元以上200万元以下的罚款；构成犯罪的，依法追究刑事责任。
<br>　　有本条例第七条规定的行为，介绍、诱骗、胁迫他人参加传销的，由工商行政管理部门责令停止违法行为，没收非法财物，没收违法所得，处10万元以上50万元以下的罚款；构成犯罪的，依法追究刑事责任。
<br>　　有本条例第七条规定的行为，参加传销的，由工商行政管理部门责令停止违法行为，可以处2000元以下的罚款。
<br>　　<b>第二十五条 </b> 工商行政管理部门依照本条例第二十四条的规定进行处罚时，可以依照有关法律、行政法规的规定，责令停业整顿或者吊销营业执照。
<br>　　<b>第二十六条 </b> 为本条例第七条规定的传销行为提供经营场所、培训场所、货源、保管、仓储等条件的，由工商行政管理部门责令停止违法行为，没收违法所得，处５万元以上50万元以下的罚款。
<br>　　为本条例第七条规定的传销行为提供互联网信息服务的，由工商行政管理部门责令停止违法行为，并通知有关部门依照《<a target="_blank" rid="chl173s112.txt" class="tips" href="/law?fn=chl173s112.txt&amp;dbt=chl">互联网信息服务管理办法</a>》予以处罚。
<br>　　<b>第二十七条 </b> 当事人擅自动用、调换、转移、损毁被查封、扣押财物的，由工商行政管理部门责令停止违法行为，处被动用、调换、转移、损毁财物价值５％以上20％以下的罚款；拒不改正的，处被动用、调换、转移、损毁财物价值１倍以上３倍以下的罚款。
<br>　　<b>第二十八条 </b> 有本条例第十条规定的行为或者拒绝、阻碍工商行政管理部门的执法人员依法查处传销行为，构成违反治安管理行为的，由公安机关依照治安管理的法律、行政法规规定处罚；构成犯罪的，依法追究刑事责任。
<br>　　<b>第二十九条 </b> 工商行政管理部门、公安机关及其工作人员滥用职权、玩忽职守、徇私舞弊，未依照本条例规定的职责和程序查处传销行为，或者发现传销行为不予查处，或者支持、包庇、纵容传销行为，构成犯罪的，对直接负责的主管人员和其他直接责任人员，依法追究刑事责任；尚不构成犯罪的，依法给予行政处分。
<br>
<br><br><div align="center"><strong>第五章  附则</strong></div>
<br>　　<b>第三十条 </b> 本条例自2005年１１月１日起施行。
<br>
<br>

<br>
				</div>
				<!--/div 摘录条款-->
				<form action="zl.htm" method="post" enctype="text/plain">
					<input type="hidden" id="fn" name="fn">
					<textarea id="slt" name="slt" style="display: none"></textarea>
				</form>
				<div id="zlbt" style="display: none; width: 55; height: 60; top: 300; left: 270; position: absolute; background-color: #CCFFFF; border: #CCCCCC thin thin thin thin; font-size: 12px;" onmousemove="MoveIn(this)" onmouseout="MoveOut(this)">
					<table width="210" border="0" cellspacing="0" cellpadding="0">
						<tbody><tr>
							<td class="bg1">
								<table width="204" border="0" align="center" cellpadding="0" cellspacing="0">
									<tbody><tr>
										<td height="25" class="menu">
											<input name="button" type="button" class="menubtn" value="摘录此条款" onclick="prezl()">
										</td>
									</tr>
									<tr>
										<td height="25" class="menu">
											<input name="button" type="button" class="menubtn" value="全库全文检索" onclick="search()">
										</td>
									</tr>
									<tr>
										<td height="25" class="menu">
											<input name="button" type="button" class="menubtn" id="correct" value="在线法规纠错">
										</td>
									</tr>
									<tr>
										<td height="25" class="menu">
											<input name="button" type="button" class="menubtn" value="复制" onclick="copy()">
										</td>
									</tr>
								</tbody></table>
							</td>
						</tr>
					</tbody></table>



				</div>
				<!--/div 摘录条款-->
				<div id="biaozhu">
					<a target="＂_blank＂" href="javascript:findLaw()" style="color:blue;">相关法律依据</a>&nbsp;&nbsp;资料提供:法律之星 引用时请对照正式文本
				</div>
			</div>
			<div id="copyright">
				版权所有：1992-2015
				北京中天诺士达科技有限责任公司&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;客服热线：010-65155090

				&nbsp;&nbsp;&nbsp;<script src="http://s4.cnzz.com/z_stat.php?id=1256116543&amp;web_id=1256116543" language="JavaScript"></script><script src="http://c.cnzz.com/core.php?web_id=1256116543&amp;t=z" charset="utf-8" type="text/javascript"></script><a href="http://www.cnzz.com/stat/website.php?web_id=1256116543" target="_blank" title="站长统计">站长统计</a>
			</div>
		</div>"""

soup = BeautifulSoup(str1,'lxml')
list = soup.find('div',class_='zhengwen').contents

str2 = ''.join(unicode(s) for s in list if not s is None)
print str2
