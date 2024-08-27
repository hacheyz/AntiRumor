package cn.edu.hit.backend.pojo;

import lombok.Data;

import java.time.LocalDate;

@Data
public class Rumor {
  private Integer id;
  private String rumor;
  private String truth;
  private String origin;
  private LocalDate publishedDate;
  private String url;

}
