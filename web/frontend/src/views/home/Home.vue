<script>
export default {
  name: "RumorInfo",
};
</script>


<template>
  <el-container class="rumor-info">

    <h1 style="font-size: 32px; color: #0e4560">谣言知识科普</h1>

    <el-main>
      <el-card class="box-card" shadow="hover">
        <section class="section">
          <h2 class="sub-header">谣言的定义</h2>
          <p>
            谣言是未经证实的、不确实的或虚假的消息或信息，通常通过口头或互联网等方式迅速传播，容易引起公众的误解和恐慌。
          </p>
        </section>
      </el-card>

      <el-card class="box-card" shadow="hover">
        <section class="section">
          <h2 class="sub-header">谣言的性质</h2>
          <ul>
            <li>虚假性：谣言通常缺乏事实依据，并且有意或无意地误导他人。</li>
            <el-divider></el-divider>
            <li>传播性：谣言通过社交媒体、口头传播等渠道迅速扩散。</li>
            <el-divider></el-divider>
            <li>隐蔽性：谣言往往披着“半真半假”的外衣，使得辨别难度增大。</li>
          </ul>
        </section>
      </el-card>

      <el-card class="box-card" shadow="hover">
        <section class="section">
          <h2 class="sub-header">谣言的影响</h2>
          <ul>
            <li>社会混乱：谣言可能引发社会恐慌、群体性事件，甚至危害社会安全。</li>
            <el-divider></el-divider>
            <li>经济损失：某些谣言会对企业、市场造成经济损失。</li>
            <el-divider></el-divider>
            <li>人际关系破坏：谣言可能损害个人或团体的声誉，破坏人际关系。</li>
          </ul>
        </section>
      </el-card>

      <el-card class="box-card" shadow="hover">
        <section class="section">
          <h2 class="sub-header">应对谣言的方法</h2>
          <ul>
            <li>查证信息来源：在传播信息前，确认其来源是否可靠。</li>
            <el-divider></el-divider>
            <li>不轻信、不传播：不轻易相信未经证实的信息，更不要随意转发谣言。</li>
            <el-divider></el-divider>
            <li>举报谣言：当发现谣言时，及时向相关部门举报，避免谣言进一步扩散。</li>
            <el-divider></el-divider>
            <li>提高媒介素养：增强对信息的鉴别能力，理性看待新闻和社交媒体上的信息。</li>
          </ul>
        </section>
      </el-card>

      <el-card class="box-card" shadow="hover">
        <section class="section">
          <h2 class="sub-header">相关法律法规</h2>
          <p>
            当前，我国的网络谣言治理涉及民法典、刑法、网络安全法、治安管理处罚法、互联网信息服务管理办法等法律和行政法规，也涉及《网络信息内容生态治理规定》《互联网群组信息服务管理规定》《互联网跟帖评论服务管理规定》等行政规章，以及地方立法中与防范虚假不实信息和谣言传播有关的内容。
          </p>
          <ul>
            <li>
              在民法层面，散布网络谣言可能会侵犯自然人或法人的名誉权，根据民法典规定，需要承担停止侵害、消除影响、赔礼道歉及赔偿损失等民事责任。
            </li>
            <el-divider></el-divider>
            <li>
              在行政法层面，如果谎报险情、疫情、警情或者以其他方法故意扰乱公共秩序，公然侮辱他人或者捏造事实诽谤他人，尚不构成犯罪的，依据治安管理处罚法等法律规定，可能受到行政拘留、罚款等行政处罚。
            </li>
            <el-divider></el-divider>
            <li>
              在刑法层面，相关行为则可能触犯编造、故意传播虚假信息罪和诽谤罪。例如，刑法规定：编造虚假的险情、疫情、灾情、警情，在信息网络或者其他媒体上传播，或者明知是上述虚假信息，故意在信息网络或者其他媒体上传播，严重扰乱社会秩序的，处三年以下有期徒刑、拘役或者管制；造成严重后果的，处三年以上七年以下有期徒刑。
            </li>
          </ul>
        </section>
      </el-card>
    </el-main>
  </el-container>
</template>

<style scoped>
.rumor-info {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

.el-header {
  background-color: #f5f5f5;
  text-align: center;
  padding: 20px;
}

h2 {
  color: #2c3e50;
  margin-bottom: 10px;
}

section {
  padding: -20px;
}

p {
  text-indent: 2em;
  color: #666;
}

.box-card {
  margin-bottom: 20px;
}

ul {

}

.sub-header {
  font-size: 24px;
  color: #08374f;
  padding-bottom: 20px;
}

li {
  padding: 10px 0; /* 增加上下内边距 */
  color: #444;
}
</style>
