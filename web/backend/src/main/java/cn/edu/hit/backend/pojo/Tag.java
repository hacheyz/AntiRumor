package cn.edu.hit.backend.pojo;

import lombok.Data;

@Data
public class Tag {
  private Integer id;
  private String name;
  // 与标签关联的Rumor条数
  private Integer relateNum;
}
